from email.mime import base
import random
import SortedPersonDescriptors
import GeneralAdjectiveList
import nounlist
import verbs_dictionaries
import split_tense
import WIP_poemnounadj
import shortPoem3resultsList
import pyttsx3
engine = pyttsx3.init() # object creation

good = 'dope', 'sick', 'suhweet', 'sweet', 'pretty awesome', 'pretty decent', 'good', 'great', 'tops', 'pretty good', 'pretty great', 'cool', 'neat', 'badass', 'neato', 'epic', 'righteous', 'real', 'solid', 'top', 'fine', 'quality', 'legit', 'enjoyable', 'nice', 'goodgood', 'gud', 'decent', 'dece', 'fair', 'bang on', 'fairish', 'okay', 'ok', 'boss', 'crackerjack', 'great', 'grooovy', 'nifty', 'stellar', 'top-notch', 'swell', 'terrific', 'tip-top', 'dandy', 'goddamn good', 'GOOD', 'aces', 'all right', 'ballin', 'bit of all right', 'bloomin good', 'bomb', 'bonanza', 'chill', 'chilled', 'killer', 'gnarly', 'hellacious', 'hella', 'radical', 'rad', 'phat', 'tubular'
time = "Last week", "Today", "Earlier", "Some time last week", "This week", "A few minutes ago", "Once"
name1 = 'abject', 'feral', 'squizzed', 'queer', 'quotidian', 'incommensurable', 'demotic', 'diachroic', 'apocryphal', 'ludic', 'the_', 'sublime', 'virtuous', 'sybaritic', 'sibilant', 'master', 'madame', 'sir', 'Lady', 'fading', 'falling', 'disappearing', 'black', 'white', 'red', 'numinous', 'dear', 'gentle', 'violent', 'last', 'numberone', 'winding', 'dream', 'your', 'rainbow', 'deep', 'rare', 'kind', 'twilight', 'dusk', 'dawn', 'endless', 'infinite', 'eternal', 'deepest', 'my_', 'stupid', 'worthless', 'selfloathing', 'awkward', 'terror', 'digital', 'mystic', 'donttrustthe', 'kissmy', 'bewarethe', 'anti_', 'dangerous', 'scared', 'occult', 'runic', 'meta', 'touchmy', 'wishing', 'heart', 'spirit', 'hate', 'sayyesto', 'saynoto', 'being', 'tight', 'spiral', 'screaming', 'cute', 'tiny', 'vast', 'cosmic', 'haunted', 'one_with_', 'god', 'goddess', 'killing', 'murder', 'crying', 'smiling', 'pretend', 'fake', 'false', 'true', 'iam', 'furry', 'spooky', 'angel', 'devil', 'lying', 'comeback', 'diaryof', 'bloody', 'blind', 'drowsy', 'lazy', 'scarlet', 'neon', 'monochrome', 'noir', 'sepia', 'long', 'broken', 'fragile', 'unbeatable', 'kitten', 'poison', 'poisoned', 'blue', 'antique', 'oldschool', 'bad', 'good', 'wellbehaved', 'spooky', 'vertical', 'horizontal', 'harmless', 'pig', 'nuclear', 'quantum', 'evil', 'dying', 'hell', 'paradise', 'terminal', 'final', 'jazz', 'glitter', 'sewer', 'screaming', 'loyal', 'ghost', 'radio', 'radioactive', 'sweet', 'confused', 'vague', 'non', 'loud', 'mute', 'silent', 'quiet', 'disco', 'artofthe', 'absent', 'panic', 'everybodys', 'overwrought', 'corporeal', 'incorporeal', 'embodied', 'disembodied', 'truth_in_', 'lies_in_', 'believe_in_', 'believe_the_', 'whynot', 'whisper', 'tedious', 'nasty', 'nightofthe', 'riseofthe', 'cantstop', 'always', 'never', 'maybe', 'sometimes', 'occasional', 'hesitant', 'open', 'burnthe', 'seizethe', 'uneasy', 'abstract', 'haunting', 'nogood', 'glittering', 'flightofthe', 'retro', 'glitchy', 'glitch', 'cyber', 'bitmap', 'VHS', 'downwith', 'empty', 'happy', 'deepest', 'widest', 'longest', 'prismatic', 'spiritual', 'uncanny', 'weird', 'common', 'naughty', 'sneaky', 'zombie', 'horror', 'techno', 'split', 'spit', 'tall', 'brown', 'big', 'shadow', 'fading', 'faded', 'mouldy', 'smouldering', 'dank', 'empirical', 'skeptical', 'team', 'findthe', 'leavethe', 'behindthe', 'behindmy', 'underyour', 'undermy', 'cantstopthe', 'ignorethe', 'listentothe', 'live', 'fake', 'burnyour', 'burythe', 'charred', 'buried', 'suffocating', 'suffocated', 'midnight', 'dawn', 'morning', 'time', 'minute', 'ticktock', 'perpetual', 'beating', 'victorian', 'after', 'easy', 'calm', 'simple', 'holy', 'sacred', 'giant', 'robot', 'we_the_', 'notthe', 'nightmare', 'distant', 'doctor', 'dr', 'lil', 'cryo', 'star', 'meteor', 'mecha', 'frankenstein', 'vampire', 'rhizomatic', 'bright', 'blight', 'fright', 'fear', 'carryon', 'ilove', 'ihate', 'skreen', 'square', 'circular', 'self', 'yearofthe', 'tomorrows', 'future', 'analog', 'eating', 'swallowmy', 'swallowyour', 'halflife', 'expired', 'missing', 'criminal', 'burglar', 'house', 'artificial', 'authentic', 'real', 'political', 'mistreated', 'misused', 'misunderstood', 'illegible', 'organic', 'wild', 'mad', 'crazy', 'insane', 'manic', 'summonsyour', 'bringmemy', 'forgotten', 'tangle', 'fizzy', 'soda', 'ego', 'spider', 'exploited', 'chaos', 'the', 'believe_in_', 'houseof', 'madaboutthe', 'whereismy', 'heartof', 'scene', 'dearest', 'doom', 'beyondthe', 'gotyour', 'night', 'corporate', 'followthe', 'sight', 'parasitic', 'living', 'dead', 'belowthe', '2bit', 'basement', 'existential', 'porcelain', 'eerie', 'snot', 'garbage', 'academic', 'unstable', 'stable', 'bit', 'byte', 'web', 'pk', 'new', 'old', 'alpha', 'beta', 'gamma', 'omega', 'bat', 'acid', 'copper', 'circuit', 'system', 'wolf', 'sombre', 'knife', 'iwant', 'little', 'le', 'grim', 'goth', '13th', 'paradox', 'blood', 'eatmy', 'avoidthe', 'el_', 'scary', 'baby', 'posh', 'shaved', 'RIP', 'Sgt', 'QT', 'CRT', 'VHS', 'bacterial', 'sweetie', 'organic'
name2 = 'avocado', 'bear', 'hunger', 'ninja', 'leitmotif', 'hermeneutic', 'wildflower', 'droplet', 'hyena', 'cynosure', 'eidos', 'telos', 'dreaming', 'dreams', 'joy', 'red', 'cat', 'eyes', 'mouth', 'lipstick', 'teeth', 'being', 'panic', 'essence', 'pebble', 'egg', 'thunder', 'storm', 'ocean', 'wave', 'wind', 'demons', '_me', '_you', 'desire', 'rage', 'melancholy', 'grief', 'wrath', 'revenge', 'throat', 'heart', 'spine', 'nerves', 'footsteps', 'sleep', 'hole', 'passage', 'jane', 'jade', 'rabbit', 'fear', 'escape', 'ghost', 'wraith', 'witch', 'fright', 'pagan', 'box', 'mythos', 'canon', 'wish', 'blink', 'well', 'swell', 'mind', 'soul', 'spirit', 'light', 'shadow', 'dark', 'darkness', 'bright', 'spiral', 'scream', 'screaming', 'screams', 'tears', 'god', 'romance', 'envy', 'greed', 'teen', 'spider', 'jellyfish', 'kitten', 'psyche', 'cosmos', 'stars', 'universe', 'people', 'sun', 'moon', 'hurt', 'pain', 'cuddles', '_us', 'them', 'society', 'tshirt', 'socks', 'barrel', 'song', 'paws', 'animal', 'angel', 'devil', 'tongue', 'surface', 'equation', 'kid', 'killer', 'totem', 'doorknob', 'basilisk', 'mirror', 'splinter', 'poison', 'pain', 'sunday', 'monday', 'wednesday', 'october', 'november', 'revolution', 'fog', 'pig', 'bird', 'hero', 'wounds', 'claws', 'monster', 'freak', 'saint', 'person', 'questions', 'spot', 'circle', 'blood', 'veins', 'sigh', 'laughter', 'spook', 'fox', 'venom', 'paper', 'beast', 'bloom', 'creep', 'water', 'rain', 'suspect', 'witness', 'passenger', 'scientist', 'voyeur', 'artist', 'liar', 'queen', 'hell', 'heaven', 'eden', 'arcadia', 'ego', 'maniac', 'victim', 'passage', 'pyramid', 'tesseract', 'hive', 'nonconformist', 'conformist', 'silence', 'thief', 'quiet', 'letter', 'disco', 'dancer', 'memory', 'photograph', 'pie', 'fruit', 'decay', 'combustion', 'context', 'threat', 'malcontent', 'discontent', 'sauce', 'spatula', 'spoon', 'dalliance', 'whispers', 'murmurs', 'click', 'sound', 'phenomena', 'problem', 'veil', 'contract', 'virtue', 'sin', 'sinner', 'priest', 'peace', 'limit', 'limits', 'influence', 'participant', 'stranger', 'friend', 'sheep', 'tentacle', 'violence', 'doll', 'clown', 'halo', 'message', 'above', 'below', 'envelope', 'pop', 'hack', 'shrug', 'skeptic', 'lover', 'enemy', 'tree', 'willow', 'oak', 'rose', 'sparrow', 'owl', 'whale', 'sunflower', 'nectar', 'trouble', 'clock', 'wall', 'face', 'nuisance', 'phantom', 'stalker', 'church', 'cross', 'hivemind', 'domino', 'panda', 'space', 'string', 'violin', 'serenade', 'shriek', 'bear', 'robot', 'cyborg', 'nightmare', 'candle', 'sense', 'shower', 'gilles', 'deleuze', 'plato', 'shelley', 'frankenstein', 'vampire', 'rhizome', 'fungi', 'mushroom', 'bacteria', 'organism', 'virus', 'carpet', 'head', 'bright', 'blight', 'broadcast', 'skreen', 'skreener', 'logic', 'madness', 'instability', 'self', 'future', 'analog', 'seed', 'oflife', 'psycho', 'criminal', 'pills', 'politics', 'daimon', 'genius', 'moss', 'parasite', 'wood', 'aperson', 'poodle', 'voyeurism', 'exploit', 'reigns', 'grass', 'nerd', 'soap', 'towel', 'handwash', 'sickness', 'gambit', 'pillow', 'drain', 'drains', 'glass', 'spiracy', 'garden', 'evidence', 'mouse', 'echidna', 'ink', 'ofdoom', 'jazz', 'free', 'bones', 'youth', 'trick', 'voice', 'patient', 'fish', 'dead', 'philosophy', 'philosopher', 'failure', 'optimist', 'skateboard', 'spice', 'splice', 'cutie', 'dude', 'inspace', 'exhibitionist', 'shack', 'writer', 'tea', 'academic', 'bag', 'cube', 'bit', 'byte', 'mega', 'mecha', 'piece', 'fan', 'bat', 'acid', 'circuit', 'system', 'garbage', 'wolf', 'tron', 'carnival', 'ophelia', 'rot', 'crow', 'fairy', 'problems', 'goth', 'paradox', 'cow', 'cycle', 'feet', 'foot', 'kiss', 'spice', 'splice', 'mathematic', 'grave', '_as_hell', 'outtahell', 'tale', 'story', 'girlfriend', 'boyfriend', 'chad', 'bee', 'sweetie', 'seed',
realname1 = 'maria', 'jonah', 'emily', 'emile', 'hannah', 'dan', 'ryan', 'chantal', 'lydia', 'henry', 'sam'
realname2 = 'walters', 'yi', 'sun', 'rogers', 'brown', 'black', 'mcgregor', 'bell',''
aka = 'more popularly known as', 'also known as', 'who goes by the handle', 'who was often referred to by friends as',
killed = 'killed', 'murdered', 'slaughtered', 'attacked', 'assaulted',
time = 'last night', 'yesterday', 'earlier this evening', 'earlier this afternoon', 'earlier today', 'today', 'last week', 'late yesterday', 'late last night', 'near midnight', 'in the early hours of the morning'
occurrence = 'a suspicious incident', 'a violent incident', 'a violent assault', 'an assault', 'an incident', 'a strange incident', 'a frightening assault', 'a blitz attack', 'a bizarre attack', 'a bizzare occurrence'
found = 'discovered', 'found', 'located', 'identified',
descriptive = 'massive', 'vicious', 'deep', 'unfamiliar', 'unidentifiable', 'mysterious', 'bizarre', 'confusing',
injurytype = 'clawmark', 'knife', 'teeth', 'bite', 'stabbing', 'crisscrossed', 'smoking',
injury = 'injuries', 'wounds', 'gashes', 'tears', 'cuts', 'gouges', 'slashes', 'lacerations', 'lesions', 'trauma',
assailant = 'an unknown assailant', 'a mysterious figure', 'a humanoid figure', 'a humanoid shape', 'a person described as running on four legs', 'a humanoid creature with wings', 'a disfigured assailant', 'a person described to have no face', 'a misshapen figure'
ending = 'Services will be announced later this week.', 'Investigations are ongoing.', 'If you have information on this incident', 'please contact local authorities.', 'More information to come.', 'We will provide updates as we receive them.'

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

def rc(list):
    return random.choice(list)

engine.say("and I am", rc(ppadj) + ",")
engine.say(rc(verbing), "down the " + rc(pnoun) + ",")
engine.say(rc(verbing) + ", " + rc(verbing) + ",")
engine.say(rc(ppadj))




engine.say("was", rc(killed), rc(time), "in", rc(occurrence), ".")
engine.say("Their body was", rc(found), "with", rc(descriptive), rc(injurytype), rc(injury), "attributed to", rc(assailant), ".")
engine.say(rc(ending))


engine.say("Hello World!")
engine.runAndWait()
engine.stop()

