import random
import SortedPersonDescriptors
import GeneralAdjectiveList
import nounlist
import verbs_dictionaries
import split_tense

hello = 'yo', 'sup', 'wattup'
perdef = SortedPersonDescriptors.person_descriptors
adj = GeneralAdjectiveList.adjective
noun = nounlist.noun
verb = verbs_dictionaries.verb
present3 = split_tense.present3rd

def rc(list):
    return random.choice(list)

print("The", rc(perdef), rc(noun), "is", rc(adj) + ",")
print("The", rc(perdef), rc(noun), rc(adj) + ",")
print("          ", rc(adj) + ",", rc(adj) + "--")
print("The", rc(noun), rc(verb), "the", rc(noun) + ".")


print ("the", rc(noun), rc(present3) + ",", rc(adj) + "...")