import constants 
import pandas as pd
from glob import glob

from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_day
from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_today
from DayReports import generate_day_report_for_today

def main():
    download_sec_bhavdata_full_for_today()
    generate_day_report_for_today()

if __name__ == "__main__":
    main()