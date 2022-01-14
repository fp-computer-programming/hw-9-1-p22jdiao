# Author: JD 01/10/2022

def find_thing(working_item, search_item):
    for i,v in enumerate(working_item):
        if v == search_item[0]:
            mark = i
            check = ""
            for x in range(len(search_item)):
                check += working_item[mark]
                mark += 1
            if check == search_item:
                return i

    return -1

x = find_thing("apple", "ple")
print(x)