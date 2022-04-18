import sys


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


def isEven(num1):
    if num1%2 == 0:
        return True

def mergeList(first, second):
    newList = []
    for x in first:
        if isEven(x):
            continue
        else:
            newList.append(x)
    
    for x in second:
        if isEven(x):
            newList.append(x)

    print(newList)
    
mergeList(list1,list2)
