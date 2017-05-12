import feather
import gzip
import json
import pandas as pd
from pathlib import Path
import statsmodels.api as sm
from subprocess import DEVNULL, STDOUT, check_call


if __name__ == '__main__':

    # Config
    DATA_DIR = Path('.') / 'data'
    url = "https://docs.google.com/spreadsheets/d/1CHMArwUdVza-ayOT1aG2tRJJfa1OWvwfMGiCu20X7Ys/export?gid=1495247060&format=csv"
    cutoff_date = '2017-01-01'

    print('Downloading from Google Sheet')
    polls = pd.read_csv(url)

    # PROCESS
    # Format percentages into decimal
    for col in ['CON', 'LAB', 'LD', 'UKIP', 'GRN', 'SNP']:
        polls[col] = polls[col].apply(lambda x: x / 100)

    # Process dates
    polls['To'] = pd.to_datetime(polls['To'])
    polls['From'] = pd.to_datetime(polls['From'])

    # Rename & rearrange columns
    party_names = ['con', 'lab', 'ld', 'ukip', 'grn']
    polls.columns = [x.lower().replace(" ", "_") for x in polls.columns]
    del polls['source']

    # Add LOWESS smoothing for 2017 data only (missing values for grn until 2016-07-05)
    polls_smoothed = polls[polls.to >= cutoff_date].groupby('to').mean().reset_index()
    for col in party_names:
        polls_smoothed[col + '_smooth'] = sm.nonparametric.lowess(polls_smoothed[col],
                                                                  polls_smoothed['to'],
                                                                  frac=0.15)[:, 1]
    polls_smoothed = polls_smoothed[['to'] + [col + '_smooth' for col in party_names]]
    polls_smoothed.columns = ['date'] + party_names

    # EXPORT
    polls.to_json(str(DATA_DIR / 'polls.json'), orient='records')
    polls.to_csv(DATA_DIR / 'polls.csv', index=False)
    feather.write_dataframe(polls, str(DATA_DIR / 'polls.feather'))

    polls_smoothed.to_json(str(DATA_DIR / 'polls_smoothed.json'), orient='records')
    polls_smoothed.to_csv(DATA_DIR / 'polls_smoothed.csv', index=False)
    feather.write_dataframe(polls_smoothed, str(DATA_DIR / 'polls_smoothed.feather'))

    # Combine polls with polls_smoothed
    combined = [
        json.loads(polls[polls.to > cutoff_date].to_json(orient='records')),
        json.loads(polls_smoothed.to_json(orient='records'))
    ]
    with open(str(DATA_DIR / 'poll_tracker.json'), 'w') as f:
        f.write(json.dumps(combined))
    with gzip.open(str(DATA_DIR / 'poll_tracker.json.gz'), 'w') as f:
        f.write(json.dumps(combined).encode('utf-8'))

    # Upload to S3
    print('Uploading to S3...')
    files_to_upload = [
        DATA_DIR / 'polls.json',
        DATA_DIR / 'polls.csv',
        DATA_DIR / 'polls.feather',
        DATA_DIR / 'polls_smoothed.json',
        DATA_DIR / 'polls_smoothed.csv',
        DATA_DIR / 'polls_smoothed.feather',
        DATA_DIR / 'poll_tracker.json',
        DATA_DIR / 'poll_tracker.json.gz',
    ]
    for file_path in files_to_upload:
        print("\t{}".format(file_path))
        key = file_path.name
        body = str(file_path.resolve())
        acl = 'public-read'
        check_call(["aws s3api put-object --bucket sixfifty --key '{0}' --body '{1}' --acl {2}".format(key, body, acl)],
                   stdout=DEVNULL, stderr=STDOUT, shell=True)
