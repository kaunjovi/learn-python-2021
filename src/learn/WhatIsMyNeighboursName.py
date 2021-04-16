# from src/learn/WhatIsMyName import print_my_name
# import WhatIsMyName
from WhatIsMyName import print_my_name_util_function

def print_name_from_this_script() : 
    print('The __name__ is ['+ __name__+']')
    print_my_name_util_function()

if __name__ == "__main__":
    print_name_from_this_script()