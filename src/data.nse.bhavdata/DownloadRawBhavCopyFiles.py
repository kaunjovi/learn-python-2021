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


df.drop(['OPEN_PRICE'], axis=1 , inplace=True)
df.drop(['HIGH_PRICE'], axis=1,  inplace=True)
df.drop(['LOW_PRICE'], axis=1, inplace=True)
df.drop(['LAST_PRICE'], axis=1, inplace=True)


# for col in df.columns:
#     print(col)


grouped_df = df.groupby(['SYMBOL'])[['TURNOVER_LACS', 'NO_OF_TRADES']].mean()

# print (grouped_df.shape)
# print (grouped_df.size)
# print (grouped_df.head(10))

# for col in grouped_df.columns:
#     print(col)

sorted_df = grouped_df.sort_values( ['TURNOVER_LACS', 'NO_OF_TRADES' ], ascending = [False,False])

print (sorted_df.head(50))