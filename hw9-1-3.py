# Author: JD 01/10/2022

def find_thing(working_item, search_item):
    for i,v in enumerate(working_item):
        if v == search_item:
            return i

    return -1

x = find_thing([0,1,2,3,4,5,6],7)
print(x)