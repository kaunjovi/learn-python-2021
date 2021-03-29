import pandas as pd
from glob import glob


RAW_BHAV_DATA_FOLDER = '/Users/kaunjovi/code/learn-python-2021/data/nse.bhavdata.0raw/'

# I would like to look at the entire dataset when I print out 
pd.set_option('display.max_rows', 2000)
pd.set_option('display.float_format', '{:,.2f}'.format)

## Now lets do some analytics on it. 

filenames = glob(RAW_BHAV_DATA_FOLDER + '*.csv')
dataframes = [pd.read_csv(f) for f in filenames]
df = pd.concat( dataframes)

## Too much data. 
## Drop a few columns for the time. 
df.drop(['OPEN_PRICE'], axis=1 , inplace=True)
df.drop(['HIGH_PRICE'], axis=1,  inplace=True)
df.drop(['LOW_PRICE'], axis=1, inplace=True)
df.drop(['LAST_PRICE'], axis=1, inplace=True)

## Fix for bad data. 

df.rename(columns=lambda x: x.strip(), inplace=True)
# df.fillna(0)

## DELIV_PER has some '-' in it. Fix them. Fix the column type. 
df['DELIV_PER'] = df['DELIV_PER'].str.strip()
df['DELIV_PER'] = df['DELIV_PER'].replace(['-'],'0.00')
df[['DELIV_PER']] = df[['DELIV_PER']].apply(pd.to_numeric)

## DELIV_QTY has some '-' in it. Fix them. Fix the column type. 
df['DELIV_QTY'] = df['DELIV_QTY'].str.strip()
df['DELIV_QTY'] = df['DELIV_QTY'].replace(['-'],'0')
df[['DELIV_QTY']] = df[['DELIV_QTY']].apply(pd.to_numeric)




# for col in grouped_df.columns:
#     print(col)

# grouped_df = df.groupby(['SYMBOL'])[['TURNOVER_LACS', 'NO_OF_TRADES']].mean()
# # sorted_df = grouped_df.sort_values( ['TURNOVER_LACS', 'NO_OF_TRADES' ], ascending = [False,False])

# for col in grouped_df.columns:
#     print(col)

grouped_df = df.groupby(['SYMBOL'])[['TURNOVER_LACS', 'DELIV_PER']].mean()
sorted_df = grouped_df.sort_values( ['TURNOVER_LACS', 'DELIV_PER' ], ascending = [False,False])
print (sorted_df.head(50))

