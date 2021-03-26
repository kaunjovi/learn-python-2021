import re

# Pull EQ only data from the MTO data files 
def pull_equity_only_data(file ):
    pattern = re.compile("^.*(,EQ,).*$")

    for i, line in enumerate(open("./raw-data-folder/" + file + ".DAT")):
        for match in re.finditer(pattern, line):
            print (match.group())


pull_equity_only_data ("MTO_15032021")


## getRawMTOData 
## prepareEQMTOData 
