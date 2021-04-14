import sys

from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_day
from DownloadRawDataFromURLs import download_sec_bhavdata_full_for_today
from DayReports import generate_day_report_for_today
from DayReports import generate_day_report

def download_and_analyse ( dates ) : 
    for date in dates :
        download_sec_bhavdata_full_for_day ( date )
        generate_day_report ( date )

if __name__ == "__main__":
    dates = sys.argv
    dates.pop(0)
    download_and_analyse(dates) 