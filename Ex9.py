


def isPalindrome(string1):
    string2 = (str(string1))[::-1]
    
    print("original number " + str(string1))

    if str(string1) == string2:
        print ("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")

#testing

isPalindrome(121)

isPalindrome(125)