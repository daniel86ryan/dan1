from email.mime import base
import random
import SortedPersonDescriptors
import GeneralAdjectiveList
import nounlist
import verbs_dictionaries
import split_tense

perdef = SortedPersonDescriptors.person_descriptors
adj = GeneralAdjectiveList.adjective
noun = nounlist.noun
verb = verbs_dictionaries.verb
basev = split_tense.base
present3 = split_tense.present3rd
verbing = split_tense.presentpart_ing

def rc(list):
    return random.choice(list)

print("In", rc(perdef), rc(noun) + "s", "we", rc(basev) + ",")
print(rc(verbing) + ",", rc(verbing) + ",")
print(rc(adj) + ".")
print("\n We", rc(basev), "with the", rc(noun) + ".")