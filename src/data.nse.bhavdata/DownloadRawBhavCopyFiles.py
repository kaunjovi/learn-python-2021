import urllib.request
import shutil
import pandas as pd
from glob import glob

DATA_URL:str = 'https://archives.nseindia.com/products/content/'
BHAV_DATA_FILE_FIRSTNAME:str = 'sec_bhavdata_full_'
BHAV_DATA_FILE_TYPE:str = '.csv'
RAW_BHAV_DATA_FOLDER = '/Users/kaunjovi/code/learn-python-2021/data/nse.bhavdata.0raw/'

# download file from url 
def download_bhavcopy_from_url(url:str):
    # print(f'Downloading bhav data from {url}')
    
    local_filename = url.split('/')[-1]
    local_filename_full = RAW_BHAV_DATA_FOLDER + local_filename

    print(f'Data being saved at {local_filename_full}')

    ## Open connection with the URL 
    ## Open a local file for writing 
    ## And write the content of URL to the local file 
    with urllib.request.urlopen(url) as response, open(local_filename_full, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    
    # print ("Saved data at ["+ file_name +"]")
    print(f'Data saved at {local_filename_full}')
    print('Success ....')

def download_bhavcopy_from_date (date:str): 
    
    FULL_BHAV_URL : str = DATA_URL+BHAV_DATA_FILE_FIRSTNAME+date+BHAV_DATA_FILE_TYPE
    print (f'Downloading the file : { FULL_BHAV_URL}')

    download_bhavcopy_from_url(FULL_BHAV_URL)



# download_bhavcopy_from_date ("15032021")
# download_bhavcopy_from_date ("16032021")
# download_bhavcopy_from_date ("17032021")
# download_bhavcopy_from_date ("18032021")
# download_bhavcopy_from_date ("19032021")
# # ============
# download_bhavcopy_from_date ("22032021")
# download_bhavcopy_from_date ("23032021")
# download_bhavcopy_from_date ("24032021")
# download_bhavcopy_from_date ("25032021")
# download_bhavcopy_from_date ('26032021')

## Now lets do some analytics on it. 

# I would like to look at the entire dataset when I print out 
pd.set_option('display.max_rows', 2000)
pd.set_option('display.float_format', '{:,.2f}'.format)

filenames = glob(RAW_BHAV_DATA_FOLDER + '*.csv')
dataframes = [pd.read_csv(f) for f in filenames]
df = pd.concat( dataframes)
df.rename(columns=lambda x: x.strip(), inplace=True)
df.fillna(0)

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




# for col in grouped_df.columns:
#     print(col)

# grouped_df = df.groupby(['SYMBOL'])[['TURNOVER_LACS', 'NO_OF_TRADES']].mean()
# # sorted_df = grouped_df.sort_values( ['TURNOVER_LACS', 'NO_OF_TRADES' ], ascending = [False,False])

# for col in grouped_df.columns:
#     print(col)

grouped_df = df.groupby(['SYMBOL'])[['TURNOVER_LACS', 'DELIV_PER']].mean()
sorted_df = grouped_df.sort_values( ['TURNOVER_LACS', 'DELIV_PER' ], ascending = [False,False])
print (sorted_df.head(50))