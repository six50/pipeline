import feather
import pandas as pd
from pathlib import Path

# Config
DATA_DIR = Path('../../')


# IMPORT
print('Importing data')

# Import general election results
ge_results = {}
file_path = DATA_DIR / 'general_election' / '2015' / 'electoral_commission' / 'results' / 'clean'
ge_results['2015'] = pd.read_csv(file_path / 'ge_2015_results.csv')

# Import EU Referendum results
file_path = DATA_DIR / 'eu_referendum' / 'electoral_commission' / 'results' / 'raw'
eu_ref = pd.read_csv(file_path / 'EU-referendum-result-data.csv')

# Aggregate EU Referendum data at Region level and derive `pc_remain` column
eu_by_region = eu_ref.groupby('Region').sum()[['Remain', 'Leave', 'Valid_Votes']].reset_index()
eu_by_region['pc_remain'] = eu_by_region['Remain'] / eu_by_region['Valid_Votes']


# MERGE
print('Merging and export')

# Pre-merge checks
match_col = 'Region'
assert(len(set(eu_by_region[match_col]).intersection(set(ge_results['2015'][match_col]))) == 12)
assert(len(set(eu_by_region[match_col]).difference(set(ge_results['2015'][match_col]))) == 0)
assert(len(set(ge_results['2015'][match_col]).difference(set(eu_by_region[match_col]))) == 0)

# Merge on Region
ge_results['2015'] = pd.merge(
    left=ge_results['2015'],
    right=eu_by_region[['Region', 'pc_remain']],
    how='left',
    on='Region'
)

# Reorder columns
cols = list(ge_results['2015'])
cols.insert(cols.index('Region') + 1,  # insert `pc_remain` col after `Region`
            cols.pop(cols.index('pc_remain')))  # remove it from current location
ge_results['2015'] = ge_results['2015'].ix[:, cols]


# EXPORT
file_path = DATA_DIR / 'model' / 'clean'
ge_results['2015'].to_csv(file_path / 'model_2015.csv', index=False)
feather.write_dataframe(ge_results['2015'], str(file_path / 'model_2015.feather'))
