import urllib.request
import shutil

# download file from url 
def download_file(url):
    local_filename = url.split('/')[-1]
    file_name = "/Users/kaunjovi/code/learn-python-2021/raw-data-folder/" + local_filename

    ## write something in the file. 
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    
    print ("Saved data at ["+ file_name +"]")

# download file based on the name of the file from nse 
def download_mto_data(mto_file_name) : 
    complete_url = "https://archives.nseindia.com/archives/equities/mto/" + mto_file_name + ".DAT"
    print ("Downloading data from ["+ complete_url+ "]")
    download_file (complete_url)    


# download MTO files for given dates 


# download_mto_data ("MTO_01032021")
# download_mto_data ("MTO_02032021")
# download_mto_data ("MTO_03032021")
# download_mto_data ("MTO_04032021")
# download_mto_data ("MTO_05032021")

# download_mto_data ("MTO_08032021")
# download_mto_data ("MTO_09032021")
# download_mto_data ("MTO_10032021")
download_mto_data ("MTO_12032021")
download_mto_data ("MTO_11032021")

# download_mto_data ("MTO_15032021")
# download_mto_data ("MTO_16032021")
# download_mto_data ("MTO_17032021")
# download_mto_data ("MTO_18032021")
# download_mto_data ("MTO_19032021")
# 
# download_mto_data ("MTO_22032021")
# download_mto_data ("MTO_23032021")
# download_mto_data ("MTO_24032021")
# download_mto_data ("MTO_25032021")