from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_day

def date_in_ddmmyyy_format(dd, mm, yyyy) : 
    dd = str(dd) 
    mm = str(mm)
    yyyy = str(yyyy)
    date = dd + mm + yyyy 
    return date.zfill(8)

def bulk_download (): 
    print ('List all the dates of the year 2020')
    yyyy = '2021'
    mm = '03'
    for dd in range(1,31): 
        date = date_in_ddmmyyy_format(dd, mm, yyyy)
        # print(date)
        download_sec_bhavdata_full_for_day(date)

if __name__ == "__main__":
    bulk_download() 