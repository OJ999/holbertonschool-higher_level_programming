#!/usr/bin/python3
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

def modify_int(num):
    num += 1

x = 5
modify_int(x)
print(x)  # Output: 5
