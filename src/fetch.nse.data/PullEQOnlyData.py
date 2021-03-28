import os
import re

def fetchDateFromMTODataFileName (fileName):
    date = fileName[4:6]
    month = fileName[6:8]
    year = fileName[8:12]
    return year + month +  date 

def modifyDataLine ( rawLine , date ): 
    return re.sub(r"^[0-9]*,[0-9]*,", date + "," , rawLine )

# Pull EQ only data from the MTO data files 
def pull_equity_only_data(file ):
    pattern = re.compile("^.*(,EQ,).*$")
    date = fetchDateFromMTODataFileName(file)
    with open("/Users/kaunjovi/code/learn-python-2021/eq-only-data-folder/" + file, 'w') as equity_only_file:
        for i, line in enumerate(open("/Users/kaunjovi/code/learn-python-2021/raw-data-folder/" + file )):
            for match in re.finditer(pattern, line):
                equityLine = match.group()
                modifiedLine = modifyDataLine (equityLine, date)
                # print (modifiedLine)
                equity_only_file.write(modifiedLine + "\n")


def prepareRawMTODataForAnalysis (folder) : 
    for filename in os.listdir(folder):
        if filename.endswith(".DAT") : 
            print ("Working on ["+filename+"]")
            pull_equity_only_data(filename)

prepareRawMTODataForAnalysis ("/Users/kaunjovi/code/learn-python-2021/raw-data-folder/")