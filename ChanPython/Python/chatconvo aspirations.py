from email.mime import base
import random
import SortedPersonDescriptors
import GeneralAdjectiveList
import nounlist
import verbs_dictionaries
import split_tense
import WIP_poemnounadj
import shortPoem3resultsList

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
topic = 'dolls', 'weird stuff', 'cute things', 'dogs', 'jambalaya'
lovewords = 'cute', 'nice', 'sweet', 'fluffy', 'adorable', 'heartmelting'
hatewords = 'gross', 'weird', 'creepy', 'smelly', 'awkward', 'feelsbadman'


def rc(list):
    return random.choice(list)

loveList = 'love', 'like', 'adore'

hateList = 'hate', 'loathe', 'despise'

def coinflip(list1, list2):
    randm = random.randint(1,2)
    if randm == 1:
        return list1
    if randm == 2:
        return list2



newNoun = rc(noun) #create new variable to hold fixed variable (noun) that is pulled from list using random function
topicList = []      #create list to store/track topics (nouns) that are pulled from lists
topicList.append(newNoun) #add new noun variable to topiclist to track that it has been used
loveOrHate = coinflip(loveList, hateList) #returns one of the two designated lists

if loveOrHate == loveList: #assign whichWords to be either lovewords or hatewords depending which loveList or hateList got called
    whichWords = lovewords
if loveOrHate == hateList:
    whichWords = hatewords

LorH1 = rc(loveOrHate) #variable/noun pulled from whichever List wins the coinflip to become loveOrHate variable (list)
niceOrMeanWord1 = rc(whichWords) #random variable 1, chosen from either lovewords or hatewords depending which List (loveList or hateList) won the coinflip
niceOrMeanWord2 = rc(whichWords) # ^ 2

while niceOrMeanWord1 == niceOrMeanWord2: #makes sure they aren't the same word
    niceOrMeanWord2 = rc(whichWords)



print("")
print("<user03> i", LorH1, newNoun + "s")
print("<puppylove> why do you", LorH1, newNoun + "s")
print("<user03> because they are", niceOrMeanWord1, "and", niceOrMeanWord2 + "!")
print("")

newNoun2 = rc(noun) #second variable to store a second topic/noun variable that is pulled from list using random function
while newNoun2 in(topicList): #logic to make sure no duplicate variables (loops until newNoun2 is not in topicList already)
    newNoun2 = rc(topic)
topicList.append(newNoun2) #add newNoun2 to topicList
