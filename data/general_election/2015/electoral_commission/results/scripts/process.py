import feather
import pandas as pd
from pathlib import Path

# Config
ROOT_DIR = Path('../')


# GENERAL ELECTION RESULTS
print('Read and clean RESULTS FOR ANALYSIS.csv')

# Import general election results
results = pd.read_csv(ROOT_DIR / 'raw' / 'RESULTS FOR ANALYSIS.csv')

# Remove 'Unnamed: 9' columnd
del results['Unnamed: 9']

# Fix bad column name (' Total number of valid votes counted ' to 'Valid Votes')
results.columns = list(results.columns[:8]) + ['Valid Votes'] + list(results.columns[9:])

# Remove rows where Constituency Name is blank
blank_rows = results['Constituency Name'].isnull()
results = results[-blank_rows].copy()

# Remove commas & coerce Electorate and Total number of valid votes counted
for col in ['Electorate', 'Valid Votes']:
    results[col] = results[col].apply(lambda x: float(x.replace(",", "")))

# Set NA vals to zero
for col in results.columns[9:]:
    results[col] = results[col].fillna(0)

# Checks
assert(results.shape == (650, 146))


# CONSTITUENCY DATA
print('Read and clean CONSTITUENCY.csv')

# Import constituency data
constituency = pd.read_csv(ROOT_DIR / 'raw' / 'CONSTITUENCY.csv', encoding='latin1')

# Remove rows where Constituency Name is blank
blank_rows = constituency['Constituency Name'].isnull()
constituency = constituency[-blank_rows].copy()

# Remove 'Unnamed: 6' columnd
del constituency['Unnamed: 6']

# Checks
assert(constituency.shape == (650, 10))


# MERGE
print('Merging and export')

# Pre-merge checks
match_col = 'Constituency ID'
assert(len(set(constituency[match_col]).intersection(set(results[match_col]))) == 650)
assert(len(set(constituency[match_col]).difference(set(results[match_col]))) == 0)
assert(len(set(results[match_col]).difference(set(constituency[match_col]))) == 0)

# Merge on Constituency ID
results = pd.merge(
    left=results,
    right=constituency[['Constituency ID', 'Region ID', 'County']],
    how='left',
    on='Constituency ID'
)

# EXPORT
column_order = ['Press Association ID Number', 'Constituency ID', 'Constituency Name', 'Constituency Type',
                'County', 'Region ID', 'Region', 'Country',  'Election Year', 'Electorate',
                'Valid Votes'] + list(results.columns[9:146])
results = results[column_order]

# Export as both CSV and Feather
file_path = ROOT_DIR / 'clean'
results.to_csv(file_path / 'ge_2015_results.csv', index=False)
feather.write_dataframe(results, str(file_path / 'ge_2015_results.feather'))
