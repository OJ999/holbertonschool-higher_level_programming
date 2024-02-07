#!/usr/bin/python3
# Mutable objects
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # Output: [1, 2, 3, 4]

# Immutable objects
x = 5
y = x
y += 1
print(x)  # Output: 5
