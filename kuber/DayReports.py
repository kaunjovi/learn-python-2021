from datetime import date
import pandas as pd
import constants 


def configure_pd() : 
    # I would like to look at the entire dataset when I print out 
    pd.set_option('display.max_rows', 2000)
    pd.set_option('display.float_format', '{:,.2f}'.format)



def create_basic_df (day): 
    ## Now lets do some analytics on it. 
    # filenames = glob( constants.RAW_DATA_FOLDER_FULL_BHAV_COPY + '*.csv')
    # dataframes = [pd.read_csv(f) for f in filenames]
    # df = pd.concat( dataframes)
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

    df.drop('PREV_CLOSE', axis='columns', inplace=True)
    df.drop('OPEN_PRICE', axis='columns', inplace=True)
    df.drop('HIGH_PRICE', axis='columns', inplace=True)
    df.drop('LOW_PRICE', axis='columns', inplace=True)
    df.drop('LAST_PRICE', axis='columns', inplace=True)


    df_equity_only = df[df['SERIES'] == 'EQ']
    # print (df.count)
    print ( df_equity_only.describe())
    print (df_equity_only[['DATE1', 'SYMBOL', 'DELIV_LACS', 'AVG_PRICE', 'DELIV_QTY', 'DELIV_PER']].sort_values('DELIV_LACS', ascending=False).head(20))

    return df 


def generate_day_report_for_today(): 
    today_in_ddmmyyyy_format = date.today().strftime('%d%m%Y') 
    generate_day_report ( today_in_ddmmyyyy_format)


def generate_day_report (day ):
    print('Generating daily reports for ' + day)
    configure_pd()
    # basic_df = 
    create_basic_df( day )

if __name__ == "__main__":
    # today_in_ddmmyyyy_format = date.today().strftime('%d%m%Y') 
    # generate_day_report(today_in_ddmmyyyy_format)
    generate_day_report('12042021')