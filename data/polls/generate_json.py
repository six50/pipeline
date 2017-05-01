import feather
import pandas as pd
from subprocess import DEVNULL, STDOUT, check_call


if __name__ == '__main__':

    print('Downloading from Google Sheet')
    url = "https://docs.google.com/spreadsheets/d/1CHMArwUdVza-ayOT1aG2tRJJfa1OWvwfMGiCu20X7Ys/export?gid=0&format=csv"
    polls = pd.read_csv(url)

    # Export
    polls.to_json('polls.json', orient='records')
    polls.to_csv('polls.csv', index=False)
    feather.write_dataframe(polls, 'polls.feather')

    # Upload to S3
    print('Uploading to S3...')
    files_to_upload = [
        'polls.json',
        'polls.csv',
        'polls.feather',
    ]
    for file_name in files_to_upload:
        print("\t{}".format(file_name))
        key = file_name
        body = file_name
        acl = 'public-read'
        check_call(["aws s3api put-object --bucket sixfifty --key '{0}' --body '{1}' --acl {2}".format(key, body, acl)],
                   stdout=DEVNULL, stderr=STDOUT, shell=True)
