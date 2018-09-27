import pandas as pd

# waOutcodesDf = pd.read_csv('./waPostcodes_outcodes.csv', sep=',', header=None, names=['no', 'date', 'postcode', 'easting', 'northing'], dtype={'no': 'object', 'date': 'object', 'postcode': 'object', 'long': 'float64', 'lat': 'float64' }, index_col='postcode')
waOutcodesDf = pd.read_csv('./waPostcodes_outcodes.csv', sep=',', header=0, index_col='postcode', dtype={'no': 'object', 'postcodeDate': 'object', 'date': 'object', 'postcode': 'object', 'latitude': 'float64', 'longitude': 'float64' })
# osPostcodesDf = pd.read_csv('./OS_postcodes_latlong.csv', sep=',', usecols=[0, 1, 2], header=0, names=['postcode', 'easting', 'northing'], dtype={'postcode': 'object', 'easting': 'float64', 'northing': 'float64' }, index_col=0)
outcodesDf = pd.read_csv('./postcode_outcodes.csv', sep=',', header=0, index_col='postcode')

waOutcodesDf.update(outcodesDf)
waOutcodesDf = waOutcodesDf.dropna()

print(waOutcodesDf.iloc[0])
# print(waOutcodesDf.loc['CH61'])

waOutcodesDf.to_csv('outcodes_latlong.csv')
