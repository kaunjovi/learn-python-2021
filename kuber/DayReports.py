from datetime import date
import pandas as pd
import constants 
import os.path

def configure_pd() : 
    # I would like to look at the entire dataset when I print out 
    pd.set_option('display.max_rows', 2000)
    pd.set_option('display.float_format', '{:,.2f}'.format)



def create_basic_df (day): 

    df = pd.read_csv ( constants.COMPLETE_BHAV_FILE_BY_DAY(day))

    df.rename(columns=lambda x: x.strip(), inplace=True)

    df['SERIES'] = df['SERIES'].str.strip()

    ## DELIV_PER has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_PER'] = df['DELIV_PER'].str.strip()
    df['DELIV_PER'] = df['DELIV_PER'].replace(['-'],'0.00')
    df[['DELIV_PER']] = df[['DELIV_PER']].apply(pd.to_numeric)

    ## DELIV_QTY has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_QTY'] = df['DELIV_QTY'].str.strip()
    df['DELIV_QTY'] = df['DELIV_QTY'].replace(['-'],'0')
    df[['DELIV_QTY']] = df[['DELIV_QTY']].apply(pd.to_numeric)

    df['DELIV_LACS'] = df.apply (lambda row: (row['TURNOVER_LACS'] * row['DELIV_PER'] )/100 , axis=1)
    df['DELIV_LACS'] = df['DELIV_LACS'].astype(int)
    # df['DELIV_LACS'].apply(pd.to_float)

    df.drop('PREV_CLOSE', axis='columns', inplace=True)
    df.drop('OPEN_PRICE', axis='columns', inplace=True)
    df.drop('HIGH_PRICE', axis='columns', inplace=True)
    df.drop('LOW_PRICE', axis='columns', inplace=True)
    df.drop('LAST_PRICE', axis='columns', inplace=True)


    df_equity_only = df[df['SERIES'] == 'EQ']
    # print (df.count)
    # print ( df_equity_only.describe())
    df_top_twenty_deliveries = df_equity_only[['DATE1', 'SYMBOL', 'DELIV_LACS', 'AVG_PRICE', 'DELIV_QTY', 'DELIV_PER']].sort_values('DELIV_LACS', ascending=False).head(20)

    # df.to_csv('check.csv')

    return df_top_twenty_deliveries


def generate_day_report_for_today(): 
    generate_day_report ( constants.TODAY())


def generate_day_report (day ):
    
    file = constants.COMPLETE_BHAV_FILE_BY_DAY(day) 

    if os.path.isfile(file) :
        #print('Generating daily reports for ' + day)
        print ('Got the file ' + file + '. Analyzing now ...')
        configure_pd()
        # basic_df = 
        df = create_basic_df( day )
        df.to_csv( constants.COMPLETE_TOPTWENTY_MONTHLY_REPORT_FILE(day) , mode='a', header=True)
    else : 
        print (file + " does not exist. Moving on.")
        return None

if __name__ == "__main__":
    # today_in_ddmmyyyy_format = date.today().strftime('%d%m%Y') 
    # generate_day_report(today_in_ddmmyyyy_format)
    generate_day_report('12042021')