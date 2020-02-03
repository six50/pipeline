import gzip
import json
from pathlib import Path
from subprocess import DEVNULL, STDOUT, check_call

import pandas as pd

import feather
import statsmodels.api as sm

if __name__ == "__main__":

    # Config
    DATA_DIR = Path(".") / "data"
    base_url = "https://docs.google.com/spreadsheets/d/1CHMArwUdVza-ayOT1aG2tRJJfa1OWvwfMGiCu20X7Ys/export"
    urls = {
        "uk": base_url + "?gid=1495247060&format=csv",
        "london": base_url + "?gid=683561754&format=csv",
        "scotland": base_url + "?gid=1896448771&format=csv",
        "wales": base_url + "?gid=2059731736&format=csv",
        "ni": base_url + "?gid=1413308295&format=csv",
    }
    cutoff_date = "2017-01-01"

    # RETRIEVE DATA
    print("Downloading from Google Sheet")
    polls = {}
    for geo in urls:
        polls[geo] = pd.read_csv(urls[geo], low_memory=False)

    # PROCESS
    # Define parties, respect ordering from Google Doc
    def get_party_names(input_list):
        # Ignore these columns
        cols_to_ignore = [
            "Company",
            "Client",
            "Type",
            "Method",
            "From",
            "To",
            "Sample Size",
            "Source",
            "PDF",
            "DataSource",
        ]
        for col_name in cols_to_ignore:
            if col_name in input_list:
                input_list.remove(col_name)
        # Slugify parties
        input_list = [x.lower().replace(" ", "_") for x in input_list]
        return input_list

    parties = {}
    for geo in urls:
        parties[geo] = get_party_names(list(polls[geo].columns))

    # Formatting
    for geo in parties:
        # Rename columns
        polls[geo].columns = [x.lower().replace(" ", "_") for x in polls[geo].columns]

        # Remove cols we don't want
        if "source" in polls[geo].columns:
            del polls[geo]["source"]

        # Format percentages into decimal
        for col in parties[geo]:
            polls[geo][col] = polls[geo][col].apply(lambda x: x / 100)

        # Process dates
        polls[geo]["to"] = pd.to_datetime(polls[geo]["to"])
        polls[geo]["from"] = pd.to_datetime(polls[geo]["from"])

    # Add LOWESS smoothing for 2017 data only
    polls_smoothed = {}
    for geo in parties:
        polls_smoothed[geo] = polls[geo][polls[geo].to >= cutoff_date].groupby("to").mean().reset_index()
        polls_smoothed[geo] = polls_smoothed[geo].ffill(limit=None).bfill(limit=None)
        for party in parties[geo]:
            polls_smoothed[geo][party + "_smooth"] = sm.nonparametric.lowess(
                polls_smoothed[geo][party], polls_smoothed[geo]["to"], frac=0.15
            )[:, 1]
        polls_smoothed[geo] = polls_smoothed[geo][["to"] + [col + "_smooth" for col in parties[geo]]]
        polls_smoothed[geo].columns = ["date"] + parties[geo]

    # EXPORT
    def multi_format_export(df, filename):
        df.to_json(str(DATA_DIR / (filename + ".json")), orient="records")
        df.to_csv(DATA_DIR / (filename + ".csv"), index=False)
        feather.write_dataframe(df, str(DATA_DIR / (filename + ".feather")))

    for geo in parties:
        filename = "polls_" + geo if geo != "uk" else "polls"
        multi_format_export(polls[geo], filename)
        multi_format_export(polls_smoothed[geo], filename + "_smoothed")

        # Combine polls with polls_smoothed
        combined = [
            json.loads(polls[geo][polls[geo].to > cutoff_date].to_json(orient="records")),
            json.loads(polls_smoothed[geo].to_json(orient="records")),
        ]
        with open(str(DATA_DIR / (filename + "_tracker" + ".json")), "w") as f:
            f.write(json.dumps(combined))
        with gzip.open(str(DATA_DIR / (filename + "_tracker" + ".json.gz")), "w") as f:
            f.write(json.dumps(combined).encode("utf-8"))

    # Upload to S3
    print("Uploading to S3...")
    files_to_upload = []
    for geo in parties:
        filename = "polls_" + geo if geo != "uk" else "polls"
        for file_format in [".json", ".csv", ".feather"]:
            files_to_upload.append(DATA_DIR / (filename + file_format))
            files_to_upload.append(DATA_DIR / (filename + "_smoothed" + file_format))
        files_to_upload.append(DATA_DIR / (filename + "_tracker.json"))
        files_to_upload.append(DATA_DIR / (filename + "_tracker.json.gz"))

    for file_path in files_to_upload:
        print("\t{}".format(file_path))
        key = file_path.name
        body = str(file_path.resolve())
        acl = "public-read"
        check_call(
            [f"aws s3api put-object --bucket sixfifty --key '{key}' --body '{body}' --acl {acl}"],
            stdout=DEVNULL,
            stderr=STDOUT,
            shell=True,
        )
