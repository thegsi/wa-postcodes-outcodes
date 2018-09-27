import pandas as pd

waOutcodesDf = pd.read_csv('./outcodes_latlong.csv', sep=',', header=0, index_col='postcode', dtype={'no': 'float64', 'postcodeDate': 'object', 'date': 'object', 'postcode': 'object', 'latitude': 'float64', 'longitude': 'float64', 'no_ordinal': 'float64' })

# binLabels = [x for x in range(1, 9)]

binLabels = list(map(chr, range(97, 123)))[:16]

waOutcodesDf['no_ordinal'] = pd.qcut(waOutcodesDf['no'], 16, labels=binLabels)

waOutcodesDf.to_csv('outcodes_latlong_ord_letters.csv')
