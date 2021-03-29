import pandas as pd
from glob import glob

## Find out how many lacs worth was delivered 
## It is a bit of an approximation 
## It is just the total trade in lacs X delivery percentage 
def deliv_lacs (row ):
    return (row['TURNOVER_LACS'] * row['DELIV_PER'] )/100

def clear_up_data_before_analysis( df ): 

    df.rename(columns=lambda x: x.strip(), inplace=True)

    ## Too much data. 
    ## Drop a few columns for the time. 
    df.drop(['OPEN_PRICE'], axis=1 , inplace=True)
    df.drop(['HIGH_PRICE'], axis=1,  inplace=True)
    df.drop(['LOW_PRICE'], axis=1, inplace=True)
    df.drop(['LAST_PRICE'], axis=1, inplace=True)

    ## DELIV_PER has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_PER'] = df['DELIV_PER'].str.strip()
    df['DELIV_PER'] = df['DELIV_PER'].replace(['-'],'0.00')
    df[['DELIV_PER']] = df[['DELIV_PER']].apply(pd.to_numeric)

    ## DELIV_QTY has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_QTY'] = df['DELIV_QTY'].str.strip()
    df['DELIV_QTY'] = df['DELIV_QTY'].replace(['-'],'0')
    df[['DELIV_QTY']] = df[['DELIV_QTY']].apply(pd.to_numeric)

    df['DELIV_LACS'] = df.apply (lambda row: deliv_lacs(row), axis=1)


## Do the analysis 

def analyse_bhav_data () : 

    RAW_BHAV_DATA_FOLDER = '/Users/kaunjovi/code/learn-python-2021/data/nse.bhavdata.0raw/'

    # I would like to look at the entire dataset when I print out 
    pd.set_option('display.max_rows', 2000)
    pd.set_option('display.float_format', '{:,.2f}'.format)

    ## Now lets do some analytics on it. 
    filenames = glob(RAW_BHAV_DATA_FOLDER + '*.csv')
    dataframes = [pd.read_csv(f) for f in filenames]
    df = pd.concat( dataframes)
    
    clear_up_data_before_analysis( df )

    # print (df.describe())

    grouped_df = df.groupby(['SYMBOL'])[['DELIV_LACS', 'DELIV_PER', 'TURNOVER_LACS' ]].mean()
    sorted_df = grouped_df.sort_values( ['DELIV_LACS' ], ascending = [False]) 
    print (sorted_df.head(30))

    # df.drop(['PREV_CLOSE'], inplace=True ) 

analyse_bhav_data()

