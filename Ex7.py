


str_x = "Emma is good developer. Emma is a writer"



def countSubstring(string1, substring1):
    y = 0
    count = 0
    length = len(substring1) #4
    for x in string1:
        if string1[y:y+length] == substring1:
            count = count + 1
        y = y + 1
    return count

num1 = str(countSubstring(str_x, "Emma"))

print("Emma appeared " + num1 + " times")