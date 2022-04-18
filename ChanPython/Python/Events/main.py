#main.py

import json
import random
from lexicon import * # Import lexicon functions
# !todo - need to make functions for grabbing new names and subjects
# !todo - need to make a way to *choose* which LEXICON is used

# >>> CREATE OUTPUT STRING
# build names
username = "<" + selectRandom(names["name1"]) + selectRandom(names["name2"]) + "> "
npc      = selectRandom(names["name1"]) + selectRandom(names["name2"])

# locate subject
subject = selectRandom(subjects["subject"]) + " "

# Make space
print("")

# String 1 - build and print
str  = username + cap("I") + w("spoke") + "with " + npc + ", "
str += w("about") + subject + per("of_all_things")
str += cap("it_was") + "a " + w("good_adj") + per("talk_noun")
str += cap("you_are_plural") + com("friends") + q("right_affirmation")
str += cap("I_thought") + w("you") + w("might") + "be " + per("interested")
print("Sentence 1:")
print(str)

#Make space
print("")

# String 2 - build and print
str  = username + cap("I") + w("spoke") + "with " + npc + ", "
str += w("about") + subject + per("of_all_things")
str += cap("it_was") + "a " + w("good_adj") + per("talk_noun")
str += cap("you_are_plural") + com("friends") + q("right_affirmation")
str += cap("I_thought") + w("you") + w("might") + "be " + per("interested")
print("Sentence 2:")
print(str)

# Make space
print("")