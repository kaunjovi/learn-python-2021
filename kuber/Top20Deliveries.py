import glob
import pandas as pd
from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_day
from DayReports import generate_day_report
import constants
import os.path


def date_in_ddmmyyy_format(dd, mm, yyyy) : 
    dd = str(dd) 
    mm = str(mm)
    yyyy = str(yyyy)
    date = dd + mm + yyyy 
    return date.zfill(8)

def top20delivery_file_exists (mm , yyyy) : 
    file = constants.COMPLETE_TOPTWENTY_MONTHLY_REPORT_FILE_MMYYYY(mm, yyyy)
    if os.path.isfile(file) :
        return True 
    else : 
        return False


def generate_top20delivery_file (dd, mm, yyyy) : 
    date = date_in_ddmmyyy_format(dd, mm, yyyy)
    # print(date)
    download_sec_bhavdata_full_for_day(date)
    generate_day_report(date)


def generate_top20delivery_files (): 

    yyyy = '2021'
    mm = '02'
    if top20delivery_file_exists(mm, yyyy) == True  : 
        print ('Top delivery file already exists for ' + mm + yyyy + '. Moving on without creating new.' )
    else : 
        for dd in range(1,31): 
            generate_top20delivery_file ( dd, mm, yyyy)

def analyse_top20delivery_files():
    # get data file names
    path =constants.TOP_TWENTY_DELIVERIES_REPORT_FOLDER
    filenames = glob.glob(path + "/*.csv")
    dfs = []
    for filename in filenames:
        dfs.append(pd.read_csv(filename))
    # Concatenate all data into one DataFrame
    big_frame = pd.concat(dfs, ignore_index=True)
    big_frame.rename(columns=lambda x: x.strip(), inplace=True)

    for col in big_frame.columns:
        print(col)
    print (big_frame.describe())
    print (big_frame.head())

if __name__ == "__main__":
    generate_top20delivery_files() 
    analyse_top20delivery_files() 