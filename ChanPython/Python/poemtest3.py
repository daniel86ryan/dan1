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

print("\n The", rc(perdef), rc(noun), "is", rc(adj) + ",")
print("The", rc(perdef), rc(noun), rc(adj) + ",")
print("          ", rc(adj) + ",", rc(adj) + "--")
print("The", rc(noun), rc(verb), "the", rc(noun) + ".")


print("\n The demon", rc(verb), rc(adj) + ".")
print ("the", rc(noun), rc(verb) + ",", rc(adj) + "...\n")