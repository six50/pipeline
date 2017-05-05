import feather
import pandas as pd
from pathlib import Path
import statsmodels.api as sm
from subprocess import DEVNULL, STDOUT, check_call


if __name__ == '__main__':

    DATA_DIR = Path('.') / 'data'

    print('Downloading from Google Sheet')
    url = "https://docs.google.com/spreadsheets/d/1CHMArwUdVza-ayOT1aG2tRJJfa1OWvwfMGiCu20X7Ys/export?gid=1495247060&format=csv"
    polls = pd.read_csv(url)

    # PROCESS
    # Format percentages into decimal
    for col in ['CON', 'LAB', 'LD', 'UKIP', 'GRN', 'Other']:
        polls[col] = polls[col].apply(lambda x: x / 100)

    # Process dates
    polls['To'] = pd.to_datetime(polls['To'])

    # Rename & rearrange columns
    party_names = ['con', 'lab', 'ld', 'ukip', 'grn']
    polls.columns = [x.lower().replace(" ", "_") for x in polls.columns]
    polls.columns = ['date' if x == 'to' else x for x in polls.columns]
    polls = polls[['company', 'client', 'date'] + party_names]

    # Add LOWESS smoothing for 2017 data only (missing values for grn until 2016-07-05)
    polls_smoothed = polls[polls.date >= '2017-01-01'].groupby('date').mean().reset_index()
    for col in party_names:
        polls_smoothed[col + '_smooth'] = sm.nonparametric.lowess(polls_smoothed[col],
                                                                  polls_smoothed['date'],
                                                                  frac=0.15)[:, 1]
    polls_smoothed = polls_smoothed[['date'] + [col + '_smooth' for col in party_names]]
    polls_smoothed.columns = ['date'] + party_names

    # EXPORT
    polls.to_json(str(DATA_DIR / 'polls.json'), orient='records')
    polls.to_csv(DATA_DIR / 'polls.csv', index=False)
    feather.write_dataframe(polls, str(DATA_DIR / 'polls.feather'))

    polls_smoothed.to_json(str(DATA_DIR / 'polls_smoothed.json'), orient='records')
    polls_smoothed.to_csv(DATA_DIR / 'polls_smoothed.csv', index=False)
    feather.write_dataframe(polls_smoothed, str(DATA_DIR / 'polls_smoothed.feather'))

    # Upload to S3
    print('Uploading to S3...')
    files_to_upload = [
        DATA_DIR / 'polls.json',
        DATA_DIR / 'polls.csv',
        DATA_DIR / 'polls.feather',
        DATA_DIR / 'polls_smoothed.json',
        DATA_DIR / 'polls_smoothed.csv',
        DATA_DIR / 'polls_smoothed.feather',
    ]
    for file_path in files_to_upload:
        print("\t{}".format(file_path))
        key = file_path.name
        body = str(file_path.resolve())
        acl = 'public-read'
        check_call(["aws s3api put-object --bucket sixfifty --key '{0}' --body '{1}' --acl {2}".format(key, body, acl)],
                   stdout=DEVNULL, stderr=STDOUT, shell=True)
