# UK Polling Data

If you have any questions about these datasets please [contact us @SixFiftyData](https://twitter.com/SixFiftyData) on Twitter.

## Sources
We directly source our data from polling companies' provided tables. Read our post, _[Building SixFifty's Election Tracker](https://sixfifty.org.uk/2017/05/21/building-sixfiftys-election-tracker/)_ to read more.

## SixFifty Cleaned Polling Datasets

The following cleaned datasets are available for download from S3 in multiple formats.

| Region | JSON | CSV | Feather |
| -- | -- | -- | -- |
| **National polling** | [`polls.json`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.json) | [`polls.csv`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.csv) | [`polls.feather`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.feather) |
| **London-only polling** | [`polls_london.json`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_london.json) | [`polls_london.csv`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_london.csv) | [`polls_london.feather`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_london.feather) |
| **Scotland-only polling** | [`polls_scotland.json`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_scotland.json) | [`polls_scotland.csv`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_scotland.csv) | [`polls_scotland.feather`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_scotland.feather) |
| **Wales-only polling** | [`polls_wales.json`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_wales.json) | [`polls_wales.csv`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_wales.csv) | [`polls_wales.feather`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_wales.feather) |
| **Northern Ireland polling** | [`polls_ni.json`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_ni.json) | [`polls_ni.csv`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_ni.csv) | [`polls_ni.feather`](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_ni.feather) |

#### Data dictionary
| Column | Type | Description |
| -- | -- | -- |
| `company` | string | Polling company name, e.g. `YouGov` |
| `client` | string | Publisher name, e.g. `Times` |
| `method` | string | Either `Online` or `Phone` |
| `from` | string | Date sampled from, e.g. `2017-05-03` |
| `to` | string | Date sampled to, e.g. `2017-05-05` |
| `sample_size` | float | Sample size of poll, e.g. `1053.0` |
| `party1` (e.g. `con`) | float | Percentage considering voting for party 1 (i.e. `con` is Conservative), e.g. `0.48` |
| `party2` (e.g. `lab`) | float | Percentage considering voting for party2 (i.e. `lab` is Labour), e.g. `0.29` |
| `...` | float | Remaining columns reference party names |
| pdf | string | URL of raw data (if available) |


## SixFifty Smoothed Polls Dataset
LOWESS smoothed poll-of-polls ([details](https://sixfifty.org.uk/2017/05/21/building-sixfiftys-election-tracker/)) are also available for download from S3 in multiple formats.

| Region | JSON | CSV | Feather |
| -- | -- | -- | -- |
| **National polling** | [polls_smoothed.json](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_smoothed.json) | [polls_smoothed.csv](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_smoothed.csv) | [polls_smoothed.feather](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_smoothed.feather) |
| **London-only polling** | [polls_london_smoothed.json](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_london_smoothed.json) | [polls_london_smoothed.csv](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_london_smoothed.csv) | [polls_london_smoothed.feather](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_london_smoothed.feather) |
| **Scotland-only polling** | [polls_scotland_smoothed.json](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_scotland_smoothed.json) | [polls_scotland_smoothed.csv](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_scotland_smoothed.csv) | [polls_scotland_smoothed.feather](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_scotland_smoothed.feather) |
| **Wales-only polling** | [polls_wales_smoothed.json](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_wales_smoothed.json) | [polls_wales_smoothed.csv](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_wales_smoothed.csv) | [polls_wales_smoothed.feather](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_wales_smoothed.feather) |
| **Northern Ireland polling** | [polls_ni_smoothed.json](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_ni_smoothed.json) | [polls_ni_smoothed.csv](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_ni_smoothed.csv) | [polls_ni_smoothed.feather](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_ni_smoothed.feather) |

#### Data dictionary
| Column | Type | Description |
| -- | -- | -- |
| `date` | string | Date (derived from `sampled_to`, e.g. `2017-05-03` |
| `party1` (e.g. `con`) | float | Smoothed value for party 1 vote intention (i..e `con` is Conservative), e.g. `0.4789333335794975` |
| `party2` (e.g. `lab`) | float | Smoothed value for party 2 vote intention (i.e. `lab` is Labour), e.g. `0.28146406464685286` |
| `...` | float | Remaining columns reference party names |

## Scripts
Executing `python generate_json.py` from this directory will:

1. Pull down the latest polling data from our manually curated Google Spreadsheet.
2. Clean & process the dataset.
3. Export the dataset into `data/` in .csv, .feather and .json formats.
4. Upload the dataset to S3 using the AWS CLI tool (n.b. you must have a valid AWS token with S3 permissions for this to work).
