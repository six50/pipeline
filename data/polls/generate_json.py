import feather
import pandas as pd
from pathlib import Path
from subprocess import DEVNULL, STDOUT, check_call


if __name__ == '__main__':

    DATA_DIR = Path('.') / 'data'

    print('Downloading from Google Sheet')
    url = "https://docs.google.com/spreadsheets/d/1CHMArwUdVza-ayOT1aG2tRJJfa1OWvwfMGiCu20X7Ys/export?gid=292271149&format=csv"
    polls = pd.read_csv(url)

    # PROCESS
    # Separate out pollster & publisher
    polls['Publisher'] = polls.Pollster.apply(lambda x: x.split('/')[-1])
    polls['Pollster'] = polls.Pollster.apply(lambda x: x.split('/')[0])

    # Split out dates
    polls['Sampled From'] = polls.Dates.apply(lambda x: x.split(' - ')[0])
    polls['Sampled To'] = polls.Dates.apply(lambda x: x.split(' - ')[-1])

    # Remove commas from sample size
    polls['Sample size'] = polls['Sample size'].apply(lambda x: float(x.replace(",", "")))

    # Format percentages into decimal
    for col in ['CON', 'LAB', 'LIB', 'UKIP', 'Green', 'Other', 'Total']:
        polls[col] = polls[col].apply(lambda x: x / 100)

    # Rename & rearrange columns
    polls.columns = [x.lower().replace(" ", "_") for x in polls.columns]
    polls = polls[['pollster', 'publisher', 'sampled_from', 'sampled_to', 'sample_size',
                   'con', 'lab', 'lib', 'ukip', 'green', 'other', 'total', 'source']]

    # EXPORT
    polls.to_json(str(DATA_DIR / 'polls.json'), orient='records')
    polls.to_csv(DATA_DIR / 'polls.csv', index=False)
    feather.write_dataframe(polls, str(DATA_DIR / 'polls.feather'))

    # Upload to S3
    print('Uploading to S3...')
    files_to_upload = [
        DATA_DIR / 'polls.json',
        DATA_DIR / 'polls.csv',
        DATA_DIR / 'polls.feather',
    ]
    for file_path in files_to_upload:
        print("\t{}".format(file_path))
        key = file_path.name
        body = str(file_path.resolve())
        acl = 'public-read'
        check_call(["aws s3api put-object --bucket sixfifty --key '{0}' --body '{1}' --acl {2}".format(key, body, acl)],
                   stdout=DEVNULL, stderr=STDOUT, shell=True)
