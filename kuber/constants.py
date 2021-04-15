from datetime import date

FULL_BHAV_URL_LOCATION = 'https://archives.nseindia.com/products/content/'
BHAV_FILE_FIRST_NAME = 'sec_bhavdata_full_'
FULL_BHAV_URL = FULL_BHAV_URL_LOCATION + BHAV_FILE_FIRST_NAME
FULL_BHAV_URL_DATE = '07042021'
FULL_BHAV_URL_FILE_EXT = '.csv'

RAW_DATA_FOLDER_FULL_BHAV_COPY = '/Users/kaunjovi/code/learn-python-2021/kuber/data/full-bhav-copy/'

TOP_TWENTY_DELIVERIES_REPORT_FOLDER = '/Users/kaunjovi/code/learn-python-2021/kuber/data/top-twenty-deliveries/'
TOP_TWENTY_DELIVERIES_REPORT_FILE = 'top_twenty_deliveries'
TOP_TWENTY_DELIVERIES_REPORT_FILE_COMPLETE = TOP_TWENTY_DELIVERIES_REPORT_FOLDER + TOP_TWENTY_DELIVERIES_REPORT_FILE

def TODAY () : 
    return date.today().strftime('%d%m%Y')

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

def get_mmyyyy (day) : 
    return day[2:8]



def COMPLETE_TOPTWENTY_MONTHLY_REPORT_FILE( day ): 
    mmyyyy = get_mmyyyy( day )
    return TOP_TWENTY_DELIVERIES_REPORT_FILE_COMPLETE + '_' + mmyyyy + '.csv'

def COMPLETE_TOPTWENTY_MONTHLY_REPORT_FILE_MMYYYY( mm, yyyy ): 
    return TOP_TWENTY_DELIVERIES_REPORT_FILE_COMPLETE + '_' + mm + yyyy + '.csv'