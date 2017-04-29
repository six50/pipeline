import pandas as pd
from pathlib import Path

# Config
DATA_DIR = Path('../raw/')

# Import general election results
ge_results = {}
ge_results['2015'] = pd.read_csv(DATA_DIR / 'RESULTS FOR ANALYSIS.csv')

# Import constituency data
constituency_info = pd.read_csv(DATA_DIR / 'CONSTITUENCY.csv', encoding='latin1')
