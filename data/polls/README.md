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
| `pollster` | string | Polling company name, e.g. `YouGov` |
| `publisher` | string | Publisher name, e.g. `Sunday Times` |
| `sampled_from` | string | Date sampled from, e.g. `27 Apr 2017` |
| `sampled_to` | string | Date sampled to, e.g. `28 Apr 2017` |
| `sample_size` | float | Total sample size, e.g. `1612.0` |
| `con` | float | Percentage considering voting Conservative, e.g. `0.44` |
| `lab` | float | Percentage considering voting Labour, e.g. `0.31` |
| `lib` | float | Percentage considering voting Liberal Democrat, e.g. `0.11` |
| `ukip` | float | Percentage considering voting UKIP, e.g. `0.06` |
| `green` | float | Percentage considering voting Green, e.g. `0.02` |
| `other` | float | Percentage considering voting for other parties, e.g. `0.06` |
| `total` | float | Total of con + lab + lib + ukip + green, `other` is derived from this, e.g. `0.94` |
| `source` | string | Poll data source |

## Scripts
Executing `python generate_json.py` from this directory will:
1. Pull down the latest polling data from our manually curated Google Spreadsheet.
2. Clean & process the dataset.
3. Export the dataset into `data/` in .csv, .feather and .json formats.
4. Upload the dataset to S3 using the AWS CLI tool (n.b. you must have a valid AWS token with S3 permissions for this to work).
