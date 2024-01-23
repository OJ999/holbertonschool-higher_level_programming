#!/usr/bin/python3

for char in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(char - (ord('a') - ord('A')) if (ord('z') - char) % 2 == 0 else char), end="")
