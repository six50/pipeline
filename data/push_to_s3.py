from pathlib import Path
from subprocess import DEVNULL, STDOUT, check_call


def main(ROOT_DIR):
    ROOT_DIR = Path(ROOT_DIR)

    # Upload into bucket
    print("Uploading to S3 bucket...")
    eu_path = ROOT_DIR / 'data' / 'eu_referendum' / 'electoral_commission' / 'results'
    ge_path = ROOT_DIR / 'data' / 'general_election' / 'electoral_commission' / 'results'
    model_path = ROOT_DIR / 'data' / 'model'

    # Define files to upload
    files_to_upload = [
        # EU Referendum
        eu_path / 'raw' / 'EU-referendum-result-data.csv',
        # General Election 2010 - RAW
        ge_path / 'raw' / 'GE2010-results-flatfile-website.xls',
        # General Election 2010 - CLEAN
        ge_path / 'clean' / 'ge_2010_results.csv',
        ge_path / 'clean' / 'ge_2010_results.feather',
        # General Election 2015 - RAW
        ge_path / 'raw' / 'RESULTS FOR ANALYSIS.csv',
        ge_path / 'raw' / 'CONSTITUENCY.csv',
        # General Election 2015 - CLEAN
        ge_path / 'clean' / 'ge_2015_results.csv',
        ge_path / 'clean' / 'ge_2015_results.feather',
        # Model
        model_path / 'clean' / 'model_2015.csv',
        model_path / 'clean' / 'model_2015.feather',
    ]

    for file_path in files_to_upload:
        print("\t{}".format(file_path))
        # boto3 is really slow?!
        key = file_path.name  # Pathlib attribute
        body = str(file_path.resolve())
        acl = 'public-read'
        check_call(["aws s3api put-object --bucket sixfifty --key '{0}' --body '{1}' --acl {2}".format(key, body, acl)],
                   stdout=DEVNULL, stderr=STDOUT, shell=True)


if __name__ == '__main__':
    main('.')
