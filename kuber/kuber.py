from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_day
from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_today
import constants 

import pandas as pd
from glob import glob

## Find out how many lacs worth was delivered 
## It is a bit of an approximation 
## It is just the total trade in lacs X delivery percentage 
def deliv_lacs (row ):
    return (row['TURNOVER_LACS'] * row['DELIV_PER'] )/100

def main():

###################################
# Step 1 : 
# Download some data. And then you can analyse. 
###################################
    # download_sec_bhavdata_full_for_day ('05042021')
    # download_sec_bhavdata_full_for_day ('06042021')
    # download_sec_bhavdata_full_for_day ('07042021')
    # download_sec_bhavdata_full_for_today()

    

    # I would like to look at the entire dataset when I print out 
    pd.set_option('display.max_rows', 2000)
    pd.set_option('display.float_format', '{:,.2f}'.format)

    ## Now lets do some analytics on it. 
    filenames = glob( constants.RAW_DATA_FOLDER_FULL_BHAV_COPY + '*.csv')
    dataframes = [pd.read_csv(f) for f in filenames]
    df = pd.concat( dataframes)

    df.rename(columns=lambda x: x.strip(), inplace=True)

        ## DELIV_PER has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_PER'] = df['DELIV_PER'].str.strip()
    df['DELIV_PER'] = df['DELIV_PER'].replace(['-'],'0.00')
    df[['DELIV_PER']] = df[['DELIV_PER']].apply(pd.to_numeric)

    ## DELIV_QTY has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_QTY'] = df['DELIV_QTY'].str.strip()
    df['DELIV_QTY'] = df['DELIV_QTY'].replace(['-'],'0')
    df[['DELIV_QTY']] = df[['DELIV_QTY']].apply(pd.to_numeric)

    df['DELIV_LACS'] = df.apply (lambda row: deliv_lacs(row), axis=1)

    # print (df.describe())

    grouped_df = df.groupby(['SYMBOL'])[['DELIV_LACS', 'DELIV_PER', 'TURNOVER_LACS' ]].mean()
    sorted_df = grouped_df.sort_values( ['DELIV_LACS' ], ascending = [False]) 
    print (sorted_df.head(30))


if __name__ == "__main__":
    main()