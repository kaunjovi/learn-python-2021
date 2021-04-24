
# input().rstrip().split()
# x = txt.rstrip(",.qsw")  -- list the chars that you want to chop off
# long_string.split()
# long_string.split(',')

# array 
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# cars = ["Ford", "Volvo", "BMW"]
# x = cars[0]
# x = len(cars)
# for x in cars:
#   print(x)
# cars.append("Honda")
# cars.pop(1)
# cars.remove("Volvo")

# Lists ( of  Tuple, Set, and Dictionary) 
# ordered, changeable, and allow duplicate values
# indexed, the first item has index [0]
# Since lists are indexed, lists can have items with the same value
# A list can contain different data types. List items can be of any data type

# thislist = list(("apple", "banana", "cherry"))
# mylist = ["apple", "banana", "cherry"]
# len(thislist)
# type(mylist)

# Tuples
# thistuple = tuple(("apple", "banana", "cherry"))
# mytuple = ("apple", "banana", "cherry")
# thistuple = ("apple",) ### OOOH - dont miss the comma at the end. 
# tuple1 = ("abc", 34, True, 40, "male")


from plus_minus import plusMinus 


def test_plus_minus() : 
    plusMinus([1,2,3])
    assert False