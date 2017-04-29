import os
from pathlib import Path
import requests
import zipfile

# Config
url = 'http://www.electoralcommission.org.uk/__data/assets/file/0004/191650/'
filename = '2015-UK-general-election-data-results-WEB.zip'
target = Path('../raw/')

# Download URL into local directory
print('Downloading {}'.format(filename))
with open(filename, 'wb') as f:
    response = requests.get(url + filename)
    f.write(response.content)

# Extract into target location
print('Extracting into {}'.format(target.resolve()))
with zipfile.ZipFile(filename, "r") as f:
    f.extractall(target)

# Delete the .zip file, we don't need it
print('Cleaning up')
os.remove(filename)
