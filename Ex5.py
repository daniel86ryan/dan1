


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def firstAndLast(list):
    #return true if first and last are the same
    first = list[0]
    last = list[len(list)-1]
    if first==last:
        print("result is True")
    else:
        print("result is False")

#testing

print("Given list: [" + str(numbers_x)[1:-1]+ "]")

firstAndLast(numbers_x)

print("Given list: [" + str(numbers_y)[1:-1]+ "]")

firstAndLast(numbers_y)