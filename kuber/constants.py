FULL_BHAV_URL_LOCATION = 'https://archives.nseindia.com/products/content/'
BHAV_FILE_FIRST_NAME = 'sec_bhavdata_full_'
FULL_BHAV_URL = FULL_BHAV_URL_LOCATION + BHAV_FILE_FIRST_NAME
FULL_BHAV_URL_DATE = '07042021'
FULL_BHAV_URL_FILE_EXT = '.csv'

RAW_DATA_FOLDER_FULL_BHAV_COPY = '/Users/kaunjovi/code/learn-python-2021/kuber/data/full-bhav-copy/'

def COMPLETE_BHAV_URL ( date ) :
    complete_bhav_url = FULL_BHAV_URL 
    complete_bhav_url += date
    complete_bhav_url += FULL_BHAV_URL_FILE_EXT
    return complete_bhav_url

def COMPLETE_BHAV_FILE ( complete_bhav_url ) :
    bhav_url_file = complete_bhav_url.split('/')[-1]

    complete_bhav_url_file = RAW_DATA_FOLDER_FULL_BHAV_COPY 
    complete_bhav_url_file += bhav_url_file
    return complete_bhav_url_file

def COMPLETE_BHAV_FILE_BY_DAY (day) : 
    complete_bhav_url_file = RAW_DATA_FOLDER_FULL_BHAV_COPY 
    complete_bhav_url_file += BHAV_FILE_FIRST_NAME
    complete_bhav_url_file += day
    complete_bhav_url_file += FULL_BHAV_URL_FILE_EXT
    return complete_bhav_url_file

