import pandas as pd
import Quandl

china = Quandl.get("FRED/POPTTLCNA173NUPN")
usa = Quandl.get("FRED/USAPOPL")
canada = Quandl.get("FRED/CANPOPL")

# Convert from thousands to millions
china = china / 1000

p = pd.concat([china, usa, canada], axis=1)
p.columns = ['china', 'usa', 'canada']

p.reset_index(inplace=True)

popmelt = pd.melt(p, id_vars='Date')

popmelt.columns = ['Date', 'ISO', 'population']

popmelt['ISO'][popmelt['ISO'] == 'china'] = 'CHN'
popmelt['ISO'][popmelt['ISO'] == 'usa'] = 'USA'
popmelt['ISO'][popmelt['ISO'] == 'canada'] = 'CAN'

popmelt.to_csv('population.csv', index=False)

languages = {'country':
             ['Canada', 'China', 'United States of America'],
             'language':
             ['English', 'Mandarin', 'English']}

ldf = pd.DataFrame(languages)
ldf.to_csv('languages.csv', index=False)
