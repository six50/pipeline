from pathlib import Path
import requests

# Config
url = 'http://www.electoralcommission.org.uk/__data/assets/file/0014/212135/'
filename = 'EU-referendum-result-data.csv'
target = Path('../raw/') / filename

# Download URL into local directory
print('Downloading into {}'.format(target.resolve()))
with open(target, 'wb') as f:
    response = requests.get(url + filename)
    f.write(response.content)
