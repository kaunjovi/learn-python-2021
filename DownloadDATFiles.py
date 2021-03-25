import urllib.request
import shutil

# download file from url 
def download_file(url):
    local_filename = url.split('/')[-1]
    file_name = "./raw-data-folder/" + local_filename

    ## write something in the file. 
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

# download file based on the name of the file from nse 
def download_mto_data(mto_file_name) : 
    download_file ("https://archives.nseindia.com/archives/equities/mto/" + mto_file_name + ".DAT")    


# download MTO files for given dates 

download_mto_data ("MTO_15032021")
download_mto_data ("MTO_16032021")
download_mto_data ("MTO_17032021")
download_mto_data ("MTO_18032021")
download_mto_data ("MTO_19032021")

download_mto_data ("MTO_22032021")
download_mto_data ("MTO_23032021")
download_mto_data ("MTO_24032021")
download_mto_data ("MTO_25032021")