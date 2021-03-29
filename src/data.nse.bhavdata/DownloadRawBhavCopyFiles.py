import urllib.request
import shutil

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

# # ============
# download_bhavcopy_from_date ("08032021")
# download_bhavcopy_from_date ("09032021")
# download_bhavcopy_from_date ("10032021")
# download_bhavcopy_from_date ("11032021")
# download_bhavcopy_from_date ('12032021')

# # ============
# download_bhavcopy_from_date ("01032021")
# download_bhavcopy_from_date ("02032021")
# download_bhavcopy_from_date ("03032021")
# download_bhavcopy_from_date ("04032021")
# download_bhavcopy_from_date ("05032021")

