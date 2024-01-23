#!/usr/bin/python3

def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char) - 32) if ord('a') <= ord(char) <= ord('z') else char, end="")
    print()

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
