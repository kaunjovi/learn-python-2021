import constants 
import urllib.request
import shutil
from datetime import date

def download_sec_bhavdata_full_for_today () : 
    today_in_ddmmyyyy_format = date.today().strftime('%d%m%Y') 
    download_sec_bhavdata_full_for_day ( today_in_ddmmyyyy_format)

def download_sec_bhavdata_full_for_day ( day ) : 
    bhav_url = constants.COMPLETE_BHAV_URL( day )
    local_bhav_file = constants.COMPLETE_BHAV_FILE ( bhav_url )

    print ('Downloading full bhavcopy and security delivereable data')
    print (' From: ' + bhav_url)
    print (' To: ' + local_bhav_file)

    ## Open connection with the URL 
    ## Open a local file for writing 
    ## And write the content of URL to the local file 
    with urllib.request.urlopen(bhav_url) as response, open(local_bhav_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


if __name__ == "__main__":
    download_sec_bhavdata_full_for_today()
