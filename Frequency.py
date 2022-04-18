import sys
import GeneralAdjectiveList_Search
import Giant_AdjectivesList_jordan_siem
import shortPoem
import shortPoem2
import shortPoem3
from collections import Counter

listWords = Giant_AdjectivesList_jordan_siem.generalList
stringPoems = shortPoem.stringPoem
resultsList = []
frequencyList = []
masterFrequencyList = []
highFrequency = []


#calculate results
for x in listWords:
    if x in stringPoems:
        resultsList.append(x)


#calculate frequency
def find_all(s, sub):
    str = s.split()
    counter = str.count(sub)
    return counter


#print results
print(resultsList)
print()

#print frequency
for x in resultsList:
    frequency = (find_all(stringPoems, x))
    for y in range(frequency):
        masterFrequencyList.append(x)


frequency = Counter(masterFrequencyList)
print(frequency)

    #if len(frequencyList) > 500 & len(frequencyList) < 1000:
    #    highFrequency.append(x)



