import sys


def countNum(limit):
    num = 1
    count = 1
    for x in range(limit):
        for x in range(count):
            sys.stdout.write(str(num) + " ")
        print()
        count = count + 1
        num = num + 1

countNum(5)

countNum(10)