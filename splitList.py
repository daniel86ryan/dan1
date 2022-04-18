myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def split(first, list1, chunkSize):
    resultList = list()
    resultList.append(list1[first])
    
    
    for i in range(first, len(list1), chunkSize):
        if i+chunkSize < len(list1):
            resultList.append(list1[i+chunkSize])
            
    print(resultList)


split(0,myList,5)