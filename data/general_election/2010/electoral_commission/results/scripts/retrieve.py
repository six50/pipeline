from pathlib import Path
import requests

# Config
url = 'http://www.electoralcommission.org.uk/__data/assets/excel_doc/0003/105726/'
filename = 'GE2010-results-flatfile-website.xls'
target = Path('../') / 'raw' / filename

# Download URL into local directory
print('Downloading into {}'.format(target.resolve()))
with open(target, 'wb') as f:
    response = requests.get(url + filename)
    f.write(response.content)
