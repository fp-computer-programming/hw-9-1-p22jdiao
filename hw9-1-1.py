# Author: JD 01/10/2022

def even_item(lst):
    new_lst = []
    for i, v in enumerate(lst):
        if i % 2 == 0:
            new_lst.append(v)
    
    return new_lst

ls = [0,1,2,3,4,5,6]

result = even_item(ls)

print(result)