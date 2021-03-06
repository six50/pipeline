# SixFifty Data Pipeline
ETL data pipeline for SixFifty modelling &amp; analytics.

## SixFifty Datasets

### Raw
| Dataset | Date | Format | Source | Licence | Download URL | Repo Path |
| -- | -- | -- | -- | -- | -- | -- |
| UK Parliament general election results | 6th May 2010 | XLS | [Electoral Commission](http://www.electoralcommission.org.uk/our-work/our-research/electoral-data) | [Open Government Licence v2.0](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/) | [GE2010-results-flatfile-website.xls](http://www.electoralcommission.org.uk/__data/assets/excel_doc/0003/105726/GE2010-results-flatfile-website.xls) | [/data/general_election/electoral_commission/results/](https://github.com/six50/pipeline/tree/master/data/general_election/electoral_commission/results/) |
| UK Parliament general election results | 7th May 2015 | CSV - Zip file | [Electoral Commission](http://www.electoralcommission.org.uk/our-work/our-research/electoral-data) | [Open Government Licence v2.0](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/) | [2015-UK-general-election-data-results-WEB.zip](http://www.electoralcommission.org.uk/__data/assets/file/0004/191650/2015-UK-general-election-data-results-WEB.zip) | [/data/general_election/electoral_commission/results/](https://github.com/six50/pipeline/tree/master/data/general_election/electoral_commission/results/) |
| EU Referendum results | 23rd June 2016 | CSV | [Electoral Commission](http://www.electoralcommission.org.uk/find-information-by-subject/elections-and-referendums/upcoming-elections-and-referendums/eu-referendum/electorate-and-count-information) | [Open Government Licence v2.0](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/) | [EU-referendum-result-data.csv](http://www.electoralcommission.org.uk/__data/assets/file/0014/212135/EU-referendum-result-data.csv) | [/data/eu_referendum/electoral_commission/results/](https://github.com/six50/pipeline/tree/master/data/eu_referendum/electoral_commission/results/) |

### Processed
We aim to provide our processed datasets in both CSV and [Feather](https://blog.rstudio.org/2016/03/29/feather/) formats.

| Dataset | Description | Download URL | Repo Path |
| -- | -- | -- | -- |
| [`ge_2010_results`](https://github.com/six50/pipeline/tree/master/data/general_election/electoral_commission/results/README.md) | Cleaner version of 2010 GE data | [CSV](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2010_results.csv), [Feather](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2010_results.feather) | [data/general_election/electoral_commission/results/clean/ge_2010_results.csv](https://github.com/six50/pipeline/tree/master/data/general_election/electoral_commission/results/README.md) |
| [`ge_2015_results`](https://github.com/six50/pipeline/tree/master/data/general_election/electoral_commission/results/README.md) | Cleaner version of 2015 GE data | [CSV](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2015_results.csv), [Feather](https://s3-eu-west-1.amazonaws.com/sixfifty/ge_2015_results.feather) | [data/general_election/electoral_commission/results/clean/ge_2015_results.csv](https://github.com/six50/pipeline/tree/master/data/general_election/electoral_commission/results/README.md) |
| [`model_2015`](https://github.com/six50/pipeline/tree/master/data/model/clean/) | Clean version of 2015 GE data along with counties and EU Referendum results at a regional level | [CSV](https://s3-eu-west-1.amazonaws.com/sixfifty/model_2015.csv), [Feather](https://s3-eu-west-1.amazonaws.com/sixfifty/model_2015.feather) | [data/model/clean/model_2015.csv](https://github.com/six50/pipeline/tree/master/data/model/clean/) |

### UK Political Polling
A manually curated set of poll results can be downloaded in a variety of formats. See [data/polls/](https://github.com/six50/pipeline/tree/master/data/polls/) for more information including a data dictionary.
- [Download as JSON](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.json)
- [Download as CSV](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.csv)
- [Download as Feather](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.feather)

### BBC Debate Logs
Created by SixFifty, includes timestamps of when each person was speaking and for how long. See [data/bbcdebate/speakers/](https://github.com/six50/pipeline/tree/master/data/bbcdebate/speakers/) for more information including a data dictionary.
- [Download as CSV](https://github.com/six50/pipeline/raw/master/data/bbcdebate/speakers/bbcdebate_log.csv)

---

## Filling this repo with data (short version)
1. Check you're running Python 3.
2. Ensure you have the Python requirements with `pip install -r requirements.txt`
3. Then cd into the repo root (where this README is located) and run the following to download, populate this repo with data and auto-clean it ready for modelling:
```
python data/generate_data.py
```

## Filling this repo with data (detailed setup instructions)
Please see [these instructions on installing Anaconda + dependencies + configuring S3 tokens](docs/setup.md).

---

## Licences
| Name | Description | Attribution Statement |
| -- | -- | -- |
| [Open Parliament Licence](http://www.parliament.uk/site-information/copyright/open-parliament-licence/) | Free to copy, publish, distribute, transmit, adapt and exploit commercially or non-commercially. See URL for full details. | Contains Parliamentary information licensed under the Open Parliament Licence v3.0. |
| [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/) | Free to copy, publish, distribute, transmit, adapt and exploit commercially and non-commercially. See URL for full details. | Contains public sector information licensed under the Open Government Licence v2.0. |
