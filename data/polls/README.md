# UK Polling Data

## Sources
- http://www.electoralcalculus.co.uk/polls.html
- http://www.markpack.org.uk/opinion-polls/

## SixFifty Cleaned Polls Dataset
The cleaned dataset is available for download in three different formats:
- `polls.json` ([download](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.json))
- `polls.csv` ([download](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.csv))
- `polls.feather` ([download](https://s3-eu-west-1.amazonaws.com/sixfifty/polls.feather))

| Column | Type | Description |
| -- | -- | -- |
| `company` | string | Polling company name, e.g. `YouGov` |
| `client` | string | Publisher name, e.g. `Times` |
| `date` | string | Date sampled to, e.g. `2017-05-03` |
| `con` | float | Percentage considering voting Conservative, e.g. `0.48` |
| `lab` | float | Percentage considering voting Labour, e.g. `0.29` |
| `ld` | float | Percentage considering voting Liberal Democrat, e.g. `0.1` |
| `ukip` | float | Percentage considering voting UKIP, e.g. `0.05` |
| `grn` | float | Percentage considering voting Green, e.g. `0.02` |

## SixFifty Smoothed Polls Dataset
Download links:
- `polls_smoothed.json` ([download](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_smoothed.json))
- `polls_smoothed.csv` ([download](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_smoothed.csv))
- `polls_smoothed.feather` ([download](https://s3-eu-west-1.amazonaws.com/sixfifty/polls_smoothed.feather))

| Column | Type | Description |
| -- | -- | -- |
| `date` | string | Date sampled to, e.g. `2017-05-03` |
| `con` | float | Smoothed value for Conservative vote intention, e.g. `0.4789333335794975` |
| `lab` | float | Smoothed value for Labour vote intention, e.g. `0.28146406464685286` |
| `ld` | float | Smoothed value for Liberal Democrat vote intention, e.g. `0.09862776104756443` |
| `ukip` | float | Smoothed value for UKIP vote intention, e.g. `0.055748373852953115` |
| `grn` | float | Smoothed value for Green vote intention, e.g. `0.02525062220421586` |

## Scripts
Executing `python generate_json.py` from this directory will:
1. Pull down the latest polling data from our manually curated Google Spreadsheet.
2. Clean & process the dataset.
3. Export the dataset into `data/` in .csv, .feather and .json formats.
4. Upload the dataset to S3 using the AWS CLI tool (n.b. you must have a valid AWS token with S3 permissions for this to work).
