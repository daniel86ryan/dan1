from email.mime import base
import random
import SortedPersonDescriptors
import GeneralAdjectiveList
import nounlist
import verbs_dictionaries
import split_tense
import WIP_poemnounadj
import shortPoem3resultsList


def rc(list):
    return random.choice(list)

good = 'dope', 'sick', 'suhweet', 'sweet', 'pretty awesome', 'pretty decent', 'good', 'great', 'tops', 'pretty good', 'pretty great', 'cool', 'neat', 'badass', 'neato', 'epic', 'righteous', 'real', 'solid', 'top', 'fine', 'quality', 'legit', 'enjoyable', 'nice', 'goodgood', 'gud', 'decent', 'dece', 'fair', 'bang on', 'fairish', 'okay', 'ok', 'boss', 'crackerjack', 'great', 'grooovy', 'nifty', 'stellar', 'top-notch', 'swell', 'terrific', 'tip-top', 'dandy', 'goddamn good', 'GOOD', 'aces', 'all right', 'ballin', 'bit of all right', 'bloomin good', 'bomb', 'bonanza', 'chill', 'chilled', 'killer', 'gnarly', 'hellacious', 'hella', 'radical', 'rad', 'phat', 'tubular'
time = "Last week", "Today", "Earlier", "Some time last week", "This week", "A few minutes ago", "Once"

perdef = SortedPersonDescriptors.person_descriptors
adj = GeneralAdjectiveList.adjective
noun = nounlist.noun
verb = verbs_dictionaries.verb
basev = split_tense.base
present3 = split_tense.present3rd
verbing = split_tense.presentpart_ing
pastv = split_tense.pastparticiple
pnoun = WIP_poemnounadj.poemnoun
padj = WIP_poemnounadj.poemadj
pronoun = 'we', 'you', 'I', "", "they",'our'
preposition = '', '', '', '', '', 'beyond', 'from', 'within', 'with', 'over', 'off', 'under', 'above', 'the', 'through', 'beyond', 'skirting', 'below', 'nearing', 'whittling', 'above',
ppadj = shortPoem3resultsList.ppadj
somethinthe = 'down the', 'over the', 'in the', 'above the', 'within the', 'inside the', 'in love with the', 'in love with', 'moving', 'moving down', 'moving across',
andiam = 'and i am', 'am i', 'i am', 'we are', 'are we', 'we', ''

adjORnoun = rc(ppadj), "a " + rc(noun)

print("and I am", rc(ppadj) + ",")
print(rc(verbing), "down the " + rc(pnoun) + ",")
print(rc(verbing) + ", " + rc(verbing) + ",")
print(rc(ppadj))

print()
print()

print(rc(andiam), rc(adjORnoun) + ",")
print(rc(verbing), rc(somethinthe),  rc(pnoun) + ",")
print(rc(verbing) + ", " + rc(verbing) + ",")
print(rc(ppadj))