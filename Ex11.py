import sys


int1 = 7536

def reverseInt(string1):
    str1 = str(string1)
    string2 = str(str1[::-1])
    for x in string2:
        sys.stdout.write(x + " ")

#testing

reverseInt(7536)