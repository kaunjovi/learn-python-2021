import configparser

def CONSTANTS():
    if not hasattr(CONSTANTS, 'config_dict'):
        config = configparser.RawConfigParser()
        config.read('kuber.properties')
        CONSTANTS.config_dict = dict(config.items('KUBER'))
        print ("I read the properties file.")
    return CONSTANTS.config_dict

if __name__ == "__main__":
    print (CONSTANTS()['sec_bhavdata_full_folder'])
    print (CONSTANTS()['sec_bhavdata_full_folder'])
    print (CONSTANTS()['sec_bhavdata_full_folder'])
    print (CONSTANTS()['sec_bhavdata_full_folder'])
    print (CONSTANTS()['sec_bhavdata_full_folder'])
    print (CONSTANTS()['sec_bhavdata_full_folder'])
    print (CONSTANTS()['sec_bhavdata_full_folder'])