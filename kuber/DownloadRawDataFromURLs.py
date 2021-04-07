import constants 
import urllib.request
import shutil
from datetime import date

def construct_complete_bhav_url ( date ) :
    complete_bhav_url = constants.FULL_BHAV_URL 
    complete_bhav_url += date
    complete_bhav_url += constants.FULL_BHAV_URL_FILE_EXT
    return complete_bhav_url

def construct_complete_bhav_url_file ( complete_bhav_url ) :
    bhav_url_file = complete_bhav_url.split('/')[-1]

    complete_bhav_url_file = constants.RAW_DATA_FOLDER_FULL_BHAV_COPY 
    complete_bhav_url_file += bhav_url_file
    return complete_bhav_url_file




def download_sec_bhavdata_full_for_today () : 
    today_in_ddmmyyyy_format = date.today().strftime('%d%m%Y') 
    download_sec_bhavdata_full ( today_in_ddmmyyyy_format)

def download_sec_bhavdata_full_for_day ( day ) : 
    download_sec_bhavdata_full ( day)
    

def download_sec_bhavdata_full ( day ) : 
    complete_bhav_url = construct_complete_bhav_url ( day )
    complete_bhav_url_file = construct_complete_bhav_url_file ( complete_bhav_url )


    print ('Downloading full bhavcopy and security delivereable data')
    print (' From: ' + complete_bhav_url)
    print (' To: ' + complete_bhav_url_file)

    ## Open connection with the URL 
    ## Open a local file for writing 
    ## And write the content of URL to the local file 
    with urllib.request.urlopen(complete_bhav_url) as response, open(complete_bhav_url_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)