import random
from random import randrange


myList = ["hello", "goodbye", "whatever"]

def toUpper(word, num): 
        x = (word[num])
        y = x.upper()
        newWord = (word[0:num]) + y + (word[(num+1):len(word)])
        print(newWord)

def pickRandom(listofwords):
    randomWord = random.choice(listofwords)
    randomIndex = randrange(len(listofwords))
    toUpper(randomWord, randomIndex)

#test
pickRandom(myList)

pickRandom(myList)