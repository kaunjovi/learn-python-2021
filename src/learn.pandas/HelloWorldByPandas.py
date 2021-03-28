import pandas as pd
from glob import glob

# I would like to look at the entire dataset when I print out 
pd.set_option('display.max_rows', 2000)
pd.set_option('display.float_format', '{:,.2f}'.format)

filenames = glob('/Users/kaunjovi/code/learn-python-2021/eq-only-data-folder/*.DAT')
dataframes = [pd.read_csv(f , header = None, names=["DATE", "TICKER", "EQ", "BOUGHT", "COLLECTED", "DELIVERY"]) for f in filenames]
df = pd.concat( dataframes)
print (df.head(10))

###########################
# Either 
#     You know the list that you want to look at 
#     So you get the data only for that list. 
# Or 
#     You are trying to find the list that you want to look at 
#     So, you are looking for things that came up consistently
#         You need the growth numbers. Come back after you have secured that data. 
#     And you also look at the buying trend 
#         Which are the ones that are being bought in numbers. 
#         Which are the ones that are being collected in numbers. 
#             Rather you want to know how much money was used to buy stuff that was collected. 
#                 But you cant get that. You can get the end price but not the price they bought it for. 
#                 So you can get an approximation. 
#                 But the approximation might not be of much use if there was a big swing that day. 
###########################

grouped_df = df.groupby(['TICKER'])['COLLECTED','DELIVERY'].mean()
big_buyers_df = grouped_df[grouped_df['COLLECTED'] > 1000000].sort_values(['DELIVERY'], ascending = False)
print (big_buyers_df.head(50))

tickerList = ['HDFC', 'HDFCBANK', 'RELIANCE' ] 
blueChips = df[df['TICKER'].isin(tickerList)]
blue_chips_grouped_by = blueChips.groupby(['TICKER'])['COLLECTED','DELIVERY'].mean()
print (blue_chips_grouped_by.head(50))

# this is the mother load 
# print (df.size)
# print (df.shape)
# print (df.head(10) )

# tickerList = ['HDFC', 'HDFCBANK', 'RELIANCE', 'HDFCLIFE' ] 
# blueChips = df[df[].isin(tickerList)]
# print(  blueChips.sort_values([1,0], ascending=[True, False]) )

# print (blueChips.groupby([1])[5].mean()) 
# print (df.groupby([1])[5].mean()) 

# group by mean of delivery percentages. 
# grouped_df = df.groupby(['TICKER'])['COLLECTED','DELIVERY'].mean().sort_values(['DELIVERY'], ascending=False)
# .sort_values([4,5], ascending=[False, False]) 
# print (grouped_df.head(50))

## 



# group by mean of delivery numbers 
# grouped_df = df.groupby([1])[4].mean().sort_values(ascending=False) 
# print (grouped_df.apply(lambda g: g[g['COLLECTED'] > 10000000]))



# print (grouped_df.shape)
# print (grouped_df.size)
# print (grouped_df.head(10))
# print (grouped_df.sort_values([0], ascending = [False] ))


# grouped_df = df.groupby([1])[5].mean()
# for name, group in grouped_df : 
#     print (name)
#     # print (df.groupby([1])[5].mean()) 
#     print (group + "\n")
# 
# You can look for only the tickers that you want. 
# tickerList = ['HDFC', 'HDFCBANK', 'RELIANCE', 'RELAXO', ] 
# newdf = df[df[2].isin(tickerList)] 

# Also sort on delivery percentage if you want. 
# newdf.sort_values(6, ascending=False, inplace=True)