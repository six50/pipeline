# UK Parliament general election results

## Source
- **6th May 2010:** http://www.electoralcommission.org.uk/our-work/our-research/electoral-data
- **7th May 2015:** http://www.electoralcommission.org.uk/our-work/our-research/electoral-data

## Raw files
- **6th May 2010:**
  - `GE2010-results-flatfile-website.xls` ([download from SixFifty S3](https://s3-eu-west-1.amazonaws.com/sixfifty/GE2010-results-flatfile-website.xls))
- **7th May 2015:**
    - `RESULTS.csv`
    - `RESULTS FOR ANALYSIS.csv` ([download from SixFifty S3](https://s3-eu-west-1.amazonaws.com/sixfifty/CONSTITUENCY.csv))
    - `CONSTITUENCY.csv`
    - `PARTY NAMES.csv`
    - `NOTES.csv`

## Cleaned files
- **6th May 2010:**
  - `ge_2010_results.csv` ([download from SixFifty S3](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2010_results.csv))
  - `ge_2010_results.feather` ([download from SixFifty S3](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2010_results.feather))
- **7th May 2015:**
  - `ge_2015_results.csv` ([download from SixFifty S3](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2015_results.csv))
  - `ge_2015_results.feather` ([download from SixFifty S3](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2015_results.feather))

## Retrieving the data
```
python retrieve_2010.py
python retrieve_2015.py
```

## Cleaning the data
```
python process_2010.py
python process_2015.py
```
