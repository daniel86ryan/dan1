


val = input("Enter string: ")
count = 0

for x in str(val):
    if (count % 2) == 0:
        print(x)
    
    count+= 1