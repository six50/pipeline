from pathlib import Path
import requests


def main(ROOT_DIR):
    """Expects ROOT_DIR to be one level above (i.e. /results/)"""

    # Config
    ROOT_DIR = Path(ROOT_DIR)
    url = 'http://www.electoralcommission.org.uk/__data/assets/excel_doc/0003/105726/'
    filename = 'GE2010-results-flatfile-website.xls'
    target = ROOT_DIR / 'raw' / filename

    # Download URL into local directory
    print('Downloading into {}'.format(target.resolve()))
    with open(target, 'wb') as f:
        response = requests.get(url + filename)
        f.write(response.content)


# If being run from inside /scripts/ folder
if __name__ == "__main__":
    main(ROOT_DIR='../')
