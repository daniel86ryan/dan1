import random


def rc(list):
    return random.choice(list)

termofaffectionfam = 'honey', 'sweetie', 'dear', 'love', 'sweetheart', 'goofball', 'my dear', 'my love', 'pet', 'cutie', 'little one', 'my little one', 'dearest', 'cutiepie', 'qt', 'qtpie', 'little', 'dear one', 'my sweet', 'piglet', 'kitten', 'bear', 'bee', 'birdie', 'bug', 'bunny', 'chick', 'chickadee', 'chinchilla', 'chunky monkey', 'cricket', 'cub', 'dove', 'ducky', 'firefly', 'guppy', 'honey badger', 'kitten', 'kitty', 'ladybug', 'lark', 'newt', 'pollywog', 'raven', 'swan', 'wiggleworm', 'wildcat', 'wildebeest', 'apple', 'blueberry', 'bun', 'cheese ball', 'cocoa puff', 'cookie', 'cupcake', 'cutie pie', 'dumpling', 'honey', 'honeybun', 'jellybean', 'lemon drop', 'lollipop', 'muffin', 'peachy', 'peanut', 'peppermint', 'pippin', 'plum', 'pudding', 'pumpkin', 'shortcake', 'snickerdoodle', 'sugar', 'sugarplum', 'sweet pea', 'sweetie pie', 'blossom', 'buttercup', 'petal', 'angel', 'chatterbox', 'boo', 'chubster', 'lovey', 'precious', 'snugglebug', 'sweetie', 'sweets', 
termofaffectionfriend = 'bud', 'pal', 'friendo', 'sweetie', 'dearheart', 'love', 'guy', 'sweetheart', 'dear', 'friend'
casualgreet = 'hi', 'hey', 'hello', 'hi there', 'hello there', 'hey there', 
toffam = rc(termofaffectionfam)

toffam_held = []
toffam_held.append(toffam)


print(rc(casualgreet), toffam, "i love you,", toffam_held[0])


topic = 'vampire', 'teeth', 'human', 'cannibal'

vampireDict = 'bloodsucky', 'hot', 'pale', 'old', 'morbid', 'immortal', 'fanged'
teethDict = 'creepy', 'hard', 'pointy', 'stained', 'long', 'beast-like', 'animal-like',
humanDict = 'awful', 'pathetic', 'full of horror', 'disgusting beasts',
cannibalDict = 'hungry', 'salty', 'chewy', 'murderous', 'empty', 'vacuous', 'ethical', 'ethically consistent'
#vampireDictPos = 'hot', 'steamy'
#vampireDictNeg = 'scary', 'bloodsucky'

hateL = 'hate', 'detest', 'abhor', 'loathe',
loveL = 'love', 'adore', 'cherish',
desireL = 'desire', 'want', 'lust for', 'long for'
amterrifiedofL = 'am terrified of', 'fear', 'am afraid of', 'am in terror of'
about = 'the way they', 'how they', 'they', 'i think about how they',  'when they', 'where they', 'thinking about how they', 'pondering over how they', 'shuddering over the way they'

thistopic = rc(topic)

myDict = {'vampire': vampireDict, 'teeth':teethDict, 'human':humanDict,'cannibal':cannibalDict}
#myDictPositive = {'vampire': vampireDictPos, 'teeth':teethDictPos, 'human':humanDictPos,'cannibal':cannibalDictPos}
#myDictNegative = {'vampire': vampireDictNeg, 'teeth':teethDictNeg, 'human':humanDictNeg,'cannibal':cannibalDictNeg}

feel = hateL, loveL, desireL, amterrifiedofL, 


print('the topic is ' + thistopic)

print(rc(myDict[thistopic]))


#print("the", rc(creature), rc(present3rd) + "...and now they are " + rc(presentpart_ing))
print("i", rc(rc(feel)), thistopic + "s, " + " they are so", rc(myDict[thistopic]), "and", rc(myDict[thistopic]))