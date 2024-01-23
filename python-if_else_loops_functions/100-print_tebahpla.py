#!/usr/bin/python3

for char in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(char if char % 2 == 0 else char - 32), end="")

print()
