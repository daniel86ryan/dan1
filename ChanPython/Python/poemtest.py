import random
import SortedPersonDescriptors
import GeneralAdjectiveList
import nounlist
import verbs_dictionaries

hello = 'yo', 'sup', 'wattup'
perdef = SortedPersonDescriptors.person_descriptors
adj = GeneralAdjectiveList.adjective
noun = nounlist.noun
verb = verbs_dictionaries.verb

def rc(list):
    return random.choice(list)

print("The", rc(perdef), rc(noun), "is", rc(adj))
print("The", rc(perdef), rc(noun), "is", rc(adj))
print("The", rc(noun), rc(verb), "the", rc(noun) + ".")
