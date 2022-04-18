import verbs_dic_seplines_original

myList = verbs_dic_seplines_original.verb

def split(first, list1, chunkSize):
    resultList = list()
    resultList.append(list1[first])
    
    
    for i in range(first, len(list1), chunkSize):
        if i+chunkSize < len(list1):
            resultList.append(list1[i+chunkSize])
            
    return resultList

base = split(0,myList,5)
present3rd = split(1,myList,5)
pastsimple = split(2,myList,5)
pastparticiple = split(3,myList,5)
presentpart_ing = split(4,myList,5)