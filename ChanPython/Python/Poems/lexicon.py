#lexicon.py

import json
import random

# >>> DEFINE FUNCTIONS
# Find Random
def selectRandom(var):
    return random.choice(var)

# Find word from list
def w(list):
    s = random.choice(lexicon[list]) + " "
    return s

# Find word from list, add .
def per(list):
    s = random.choice(lexicon[list]) + ". "
    return s

# Find word from list, capitalize
def cap(list):
    s = random.choice(lexicon[list]) + " "
    return s.capitalize()

# Find word from list, add ,
def com(list):
    return random.choice(lexicon[list]) + ", "

# Find word from list, add ?
def q(list):
    return random.choice(lexicon[list]) + "? "

# Find word from list, add !
def x(list):
    return random.choice(lexicon[list]) + "! "


# >>> LOAD FILE LISTS
# files are located in the GMS2 folder, for shared use
# names list
file_name = "GMS2/datafiles/json/names.json"
with open(file_name) as f:
    names = json.load(f)

# subject list
file_name = "GMS2/datafiles/json/lexicon_subject.json"
with open(file_name) as f:
    subjects = json.load(f)

# lexicon - random articulate or casual
file_list = ["GMS2/datafiles/json/lexicon_articulate.json", "GMS2/datafiles/json/lexicon_casual.json"]
file_name = selectRandom(file_list)
with open(file_name) as f:
    lexicon = json.load(f)