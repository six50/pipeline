# SixFifty Data Pipeline
ETL data pipeline for SixFifty modelling &amp; analytics.

Dataset sources can be found under [docs](docs/datasets.md).

## Filling this repo with data (short version)
1. Check you're running Python 3.
2. Ensure you have the Python requirements with `pip install -r requirements.txt`
3. Then cd into the repo root (where this README is located) and run the following to download, populate this repo with data and auto-clean it ready for modelling:
```
python data/generate_data.py
```

## Filling this repo with data (detailed setup instructions)
Please see [these instructions on installing Anaconda + dependencies + configuring S3 tokens](docs/setup.md).

## Licences
| Name | Description | Attribution Statement |
| -- | -- | -- |
| [Open Parliament Licence](http://www.parliament.uk/site-information/copyright/open-parliament-licence/) | Free to copy, publish, distribute, transmit, adapt and exploit commercially or non-commercially. See URL for full details. | Contains Parliamentary information licensed under the Open Parliament Licence v3.0. |
| [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/) | Free to copy, publish, distribute, transmit, adapt and exploit commercially and non-commercially. See URL for full details. | Contains public sector information licensed under the Open Government Licence v2.0. |
