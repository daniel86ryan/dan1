import pathlib

currentNum = 0
prevNum = 0


for x in range(10):
    x = (currentNum + prevNum)
    print("Current Number " + str(currentNum) + " Previous Number " + str(prevNum) + " Sum: " + str(x))
    prevNum = currentNum
    currentNum+= 1


