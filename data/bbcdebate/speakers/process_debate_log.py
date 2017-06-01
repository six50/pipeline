import datetime
import numpy as np
import pandas as pd


# Import raw data
log = pd.read_csv('bbcdebate_log_raw.csv', header=None, names=['timestamp', 'speaking'])

lookups = {
    # Speakers
    '.': ('chair', 'BBC', 'Mishal Husain'),
    'p': ('party', 'Plaid Cymru', 'Leanne Wood'),
    'g': ('party', 'Green', 'Caroline Lucas'),
    'c': ('party', 'Conservatives', 'Amber Rudd'),
    'l': ('party', 'Labour', 'Jeremy Corbyn'),
    'u': ('party', 'UKIP', 'Paul Nuttall'),
    's': ('party', 'SNP', 'Angus Robertson'),
    'ld': ('party', 'Liberal Democrats', 'Tim Farron'),
    # Sections
    'opening': ('section', 'Opening statements', ''),
    'q1 - how are you going to help working people': ('section', 'Question 1 - Living standards', ''),
    'q2 - how would we have the workers and skills we need to make uk a success after brexit': ('section', 'Question 2 - Brexit', ''),  # noqa
    'q3 - where is the money coming from for our public services and how can we trust your plans add up': ('section', 'Question 3 - Public services', ''),  # noqa
    'q4 - what are your priorities for making britain a safer country and the world a safer place': ('section', 'Question 4 - Security'),  # noqa
    'q5 - how will panellists deal with trump pulling out of climate change agreement': ('section', 'Question 5 - Climate change and Trump', ''),  # noqa
    'q6 - in what way does your leadership have the talent and character needed to take this country forward': ('section', 'Question 6 - Leadership', ''),  # noqa
    'closing remarks': ('section', 'Closing statements', ''),
    'credits': ('section', 'Credits', ''),
    # Meta / markets
    'start': ('marker', '', ''),
    'end': ('marker', '', ''),
    'pause': ('marker', '', ''),
    'restart': ('marker', '', ''),
    'test': ('marker', '', ''),
}

# Lookup type/party/speaker/section + forward fill section data
log['type'] = log.speaking.apply(lambda x: lookups[x][0])
log['party'] = log.apply(lambda row: lookups[row['speaking']][1] if row['type'] == 'party' else np.nan, axis=1)
log['speaker'] = log.apply(lambda row: lookups[row['speaking']][2] if row['type'] in ['party', 'chair'] else np.nan, axis=1)  # noqa
log['section'] = log.apply(lambda row: lookups[row['speaking']][1] if row['type'] == 'section' else np.nan, axis=1)
log['section'].ffill(limit=None, inplace=True)
log.loc[log.section.isnull(), 'section'] = 'Opening credits'

# Remove markers and sections
log = log[log.type != 'section'].copy().reset_index(drop=True)

# Enforce unique timestamps - add one second to any record that has timestamp as one above
log['timestamp'] = pd.to_datetime(log.timestamp)
for i, row in log.iterrows():
    if i > 0 and log.iloc[i].timestamp == log.iloc[i-1].timestamp:
        log.ix[i, 'timestamp'] += datetime.timedelta(seconds=1)

# Check
# sum(log.timestamp.duplicated())

# Add time counter for each record (time diff between one record and next)
log['counter'] = np.nan
for i, row in log.iterrows():
    if i < len(log) - 1:
        log.ix[i, 'counter'] = (log.iloc[i + 1].timestamp - log.iloc[i].timestamp).total_seconds()

# Raw data includes a number of pause/restart records (I was doing this on a train...!)
log = log[log.speaking != 'pause'].copy().reset_index(drop=True)
log = log[log.speaking != 'test'].copy().reset_index(drop=True)
# Any restart's time needs to be added to record above
for i, row in log.iterrows():
    if i > 0 and log.iloc[i].speaking == 'restart':
        log.ix[i-1, 'counter'] += log.iloc[i].counter
# Drop markers
log = log[log.type != 'marker'].copy().reset_index(drop=True)

# Check (sums to almost exactly 90 minutes, pretty good in my books)
# log.counter.sum() / 60

# Drop speaking/type cols
del log['speaking']
del log['type']

# Add total time elapsed since event begun
log['time_elapsed'] = log.counter.cumsum()

# Recalculate record timestamps assuming a 7:30pm start time
start_time = pd.to_datetime('2017-05-31 19:30:00')
log.loc[0, 'timestamp'] = start_time
log.loc[1:, 'timestamp'] = log.time_elapsed.apply(lambda x: start_time + datetime.timedelta(seconds=x)).iloc[:-1].values

# Export as CSV
log.to_csv('bbcdebate_log.csv', header=True, index=False)
