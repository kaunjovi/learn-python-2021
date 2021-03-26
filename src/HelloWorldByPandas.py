import pandas as pd

df = pd.read_csv('./eq-only-data-folder/MTO_25032021.DAT', header = None)

# You can look for only the tickers that you want. 
tickerList = ['HDFC', 'HDFCBANK', 'RELIANCE', 'RELAXO', ] 
newdf = df[df[2].isin(tickerList)] 

# Also sort on delivery percentage if you want. 
newdf.sort_values(6, ascending=False, inplace=True)
print(newdf.head(100))