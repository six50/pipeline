import pandas as pd
from subprocess import DEVNULL, STDOUT, check_call


if __name__ == '__main__':

    url = "https://docs.google.com/spreadsheets/d/1CHMArwUdVza-ayOT1aG2tRJJfa1OWvwfMGiCu20X7Ys/export?gid=0&format=csv"
    polls = pd.read_csv(url)
    file_name = 'polls.json'
    polls.to_json(file_name, orient='records')

    # Upload to S3
    key = file_name
    body = file_name
    acl = 'public-read'
    check_call(["aws s3api put-object --bucket sixfifty --key '{0}' --body '{1}' --acl {2}".format(key, body, acl)],
               stdout=DEVNULL, stderr=STDOUT, shell=True)
