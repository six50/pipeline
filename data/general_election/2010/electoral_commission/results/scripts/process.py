import feather
import pandas as pd
from pathlib import Path


def main(ROOT_DIR):
    """Expects ROOT_DIR to be one level above (i.e. /results/)"""

    # Import
    print('Read and clean GE2010-results-flatfile-website.xls')
    ROOT_DIR = Path(ROOT_DIR)
    results = pd.read_excel(ROOT_DIR / 'raw' / 'GE2010-results-flatfile-website.xls',
                            sheetname='Party vote share')

    # Remove rows where Constituency Name is blank
    blank_rows = results['Constituency Name'].isnull()
    results = results[-blank_rows].copy()

    # Set NA vals to zero
    for col in results.columns[6:]:
        results[col] = results[col].fillna(0)

    # Checks
    assert(results.shape == (650, 144))

    # Export as both CSV and Feather
    file_path = ROOT_DIR / 'clean'
    print('Exporting to {}'.format(file_path.resolve()))
    results.to_csv(file_path / 'ge_2010_results.csv', index=False)
    feather.write_dataframe(results, str(file_path / 'ge_2010_results.feather'))


# If being run from inside /scripts/ folder
if __name__ == "__main__":
    main(ROOT_DIR='../')
