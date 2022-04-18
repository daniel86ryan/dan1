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
import sentimentwords

myList = sentimentwords.movement

def split(first, list1, chunkSize):
    resultList = list()
    resultList.append(list1[first])
    
    
    for i in range(first, len(list1), chunkSize):
        if i+chunkSize < len(list1):
            resultList.append(list1[i+chunkSize])
            
    return resultList


def rc(list):
    return random.choice(list)

base = split(0,myList,5)
present3rd = split(1,myList,5)
pastsimple = split(2,myList,5)
pastparticiple = split(3,myList,5)
presentpart_ing = split(4,myList,5)

engine = pyttsx3.init() # object creation

name1 = 'abject', 'feral', 'squizzed', 'queer', 'quotidian', 'incommensurable', 'demotic', 'diachroic', 'apocryphal', 'ludic', 'the_', 'sublime', 'virtuous', 'sybaritic', 'sibilant', 'master', 'madame', 'sir', 'Lady', 'fading', 'falling', 'disappearing', 'black', 'white', 'red', 'numinous', 'dear', 'gentle', 'violent', 'last', 'numberone', 'winding', 'dream', 'your', 'rainbow', 'deep', 'rare', 'kind', 'twilight', 'dusk', 'dawn', 'endless', 'infinite', 'eternal', 'deepest', 'my_', 'stupid', 'worthless', 'selfloathing', 'awkward', 'terror', 'digital', 'mystic', 'donttrustthe', 'kissmy', 'bewarethe', 'anti_', 'dangerous', 'scared', 'occult', 'runic', 'meta', 'touchmy', 'wishing', 'heart', 'spirit', 'hate', 'sayyesto', 'saynoto', 'being', 'tight', 'spiral', 'screaming', 'cute', 'tiny', 'vast', 'cosmic', 'haunted', 'one_with_', 'god', 'goddess', 'killing', 'murder', 'crying', 'smiling', 'pretend', 'fake', 'false', 'true', 'iam', 'furry', 'spooky', 'angel', 'devil', 'lying', 'comeback', 'diaryof', 'bloody', 'blind', 'drowsy', 'lazy', 'scarlet', 'neon', 'monochrome', 'noir', 'sepia', 'long', 'broken', 'fragile', 'unbeatable', 'kitten', 'poison', 'poisoned', 'blue', 'antique', 'oldschool', 'bad', 'good', 'wellbehaved', 'spooky', 'vertical', 'horizontal', 'harmless', 'pig', 'nuclear', 'quantum', 'evil', 'dying', 'hell', 'paradise', 'terminal', 'final', 'jazz', 'glitter', 'sewer', 'screaming', 'loyal', 'ghost', 'radio', 'radioactive', 'sweet', 'confused', 'vague', 'non', 'loud', 'mute', 'silent', 'quiet', 'disco', 'artofthe', 'absent', 'panic', 'everybodys', 'overwrought', 'corporeal', 'incorporeal', 'embodied', 'disembodied', 'truth_in_', 'lies_in_', 'believe_in_', 'believe_the_', 'whynot', 'whisper', 'tedious', 'nasty', 'nightofthe', 'riseofthe', 'cantstop', 'always', 'never', 'maybe', 'sometimes', 'occasional', 'hesitant', 'open', 'burnthe', 'seizethe', 'uneasy', 'abstract', 'haunting', 'nogood', 'glittering', 'flightofthe', 'retro', 'glitchy', 'glitch', 'cyber', 'bitmap', 'VHS', 'downwith', 'empty', 'happy', 'deepest', 'widest', 'longest', 'prismatic', 'spiritual', 'uncanny', 'weird', 'common', 'naughty', 'sneaky', 'zombie', 'horror', 'techno', 'split', 'spit', 'tall', 'brown', 'big', 'shadow', 'fading', 'faded', 'mouldy', 'smouldering', 'dank', 'empirical', 'skeptical', 'team', 'findthe', 'leavethe', 'behindthe', 'behindmy', 'underyour', 'undermy', 'cantstopthe', 'ignorethe', 'listentothe', 'live', 'fake', 'burnyour', 'burythe', 'charred', 'buried', 'suffocating', 'suffocated', 'midnight', 'dawn', 'morning', 'time', 'minute', 'ticktock', 'perpetual', 'beating', 'victorian', 'after', 'easy', 'calm', 'simple', 'holy', 'sacred', 'giant', 'robot', 'we_the_', 'notthe', 'nightmare', 'distant', 'doctor', 'dr', 'lil', 'cryo', 'star', 'meteor', 'mecha', 'frankenstein', 'vampire', 'rhizomatic', 'bright', 'blight', 'fright', 'fear', 'carryon', 'ilove', 'ihate', 'skreen', 'square', 'circular', 'self', 'yearofthe', 'tomorrows', 'future', 'analog', 'eating', 'swallowmy', 'swallowyour', 'halflife', 'expired', 'missing', 'criminal', 'burglar', 'house', 'artificial', 'authentic', 'real', 'political', 'mistreated', 'misused', 'misunderstood', 'illegible', 'organic', 'wild', 'mad', 'crazy', 'insane', 'manic', 'summonsyour', 'bringmemy', 'forgotten', 'tangle', 'fizzy', 'soda', 'ego', 'spider', 'exploited', 'chaos', 'the', 'believe_in_', 'houseof', 'madaboutthe', 'whereismy', 'heartof', 'scene', 'dearest', 'doom', 'beyondthe', 'gotyour', 'night', 'corporate', 'followthe', 'sight', 'parasitic', 'living', 'dead', 'belowthe', '2bit', 'basement', 'existential', 'porcelain', 'eerie', 'snot', 'garbage', 'academic', 'unstable', 'stable', 'bit', 'byte', 'web', 'pk', 'new', 'old', 'alpha', 'beta', 'gamma', 'omega', 'bat', 'acid', 'copper', 'circuit', 'system', 'wolf', 'sombre', 'knife', 'iwant', 'little', 'le', 'grim', 'goth', '13th', 'paradox', 'blood', 'eatmy', 'avoidthe', 'el_', 'scary', 'baby', 'posh', 'shaved', 'RIP', 'Sgt', 'QT', 'CRT', 'VHS', 'bacterial', 'sweetie', 'organic'
name2 = 'avocado', 'bear', 'hunger', 'ninja', 'leitmotif', 'hermeneutic', 'wildflower', 'droplet', 'hyena', 'cynosure', 'eidos', 'telos', 'dreaming', 'dreams', 'joy', 'red', 'cat', 'eyes', 'mouth', 'lipstick', 'teeth', 'being', 'panic', 'essence', 'pebble', 'egg', 'thunder', 'storm', 'ocean', 'wave', 'wind', 'demons', '_me', '_you', 'desire', 'rage', 'melancholy', 'grief', 'wrath', 'revenge', 'throat', 'heart', 'spine', 'nerves', 'footsteps', 'sleep', 'hole', 'passage', 'jane', 'jade', 'rabbit', 'fear', 'escape', 'ghost', 'wraith', 'witch', 'fright', 'pagan', 'box', 'mythos', 'canon', 'wish', 'blink', 'well', 'swell', 'mind', 'soul', 'spirit', 'light', 'shadow', 'dark', 'darkness', 'bright', 'spiral', 'scream', 'screaming', 'screams', 'tears', 'god', 'romance', 'envy', 'greed', 'teen', 'spider', 'jellyfish', 'kitten', 'psyche', 'cosmos', 'stars', 'universe', 'people', 'sun', 'moon', 'hurt', 'pain', 'cuddles', '_us', 'them', 'society', 'tshirt', 'socks', 'barrel', 'song', 'paws', 'animal', 'angel', 'devil', 'tongue', 'surface', 'equation', 'kid', 'killer', 'totem', 'doorknob', 'basilisk', 'mirror', 'splinter', 'poison', 'pain', 'sunday', 'monday', 'wednesday', 'october', 'november', 'revolution', 'fog', 'pig', 'bird', 'hero', 'wounds', 'claws', 'monster', 'freak', 'saint', 'person', 'questions', 'spot', 'circle', 'blood', 'veins', 'sigh', 'laughter', 'spook', 'fox', 'venom', 'paper', 'beast', 'bloom', 'creep', 'water', 'rain', 'suspect', 'witness', 'passenger', 'scientist', 'voyeur', 'artist', 'liar', 'queen', 'hell', 'heaven', 'eden', 'arcadia', 'ego', 'maniac', 'victim', 'passage', 'pyramid', 'tesseract', 'hive', 'nonconformist', 'conformist', 'silence', 'thief', 'quiet', 'letter', 'disco', 'dancer', 'memory', 'photograph', 'pie', 'fruit', 'decay', 'combustion', 'context', 'threat', 'malcontent', 'discontent', 'sauce', 'spatula', 'spoon', 'dalliance', 'whispers', 'murmurs', 'click', 'sound', 'phenomena', 'problem', 'veil', 'contract', 'virtue', 'sin', 'sinner', 'priest', 'peace', 'limit', 'limits', 'influence', 'participant', 'stranger', 'friend', 'sheep', 'tentacle', 'violence', 'doll', 'clown', 'halo', 'message', 'above', 'below', 'envelope', 'pop', 'hack', 'shrug', 'skeptic', 'lover', 'enemy', 'tree', 'willow', 'oak', 'rose', 'sparrow', 'owl', 'whale', 'sunflower', 'nectar', 'trouble', 'clock', 'wall', 'face', 'nuisance', 'phantom', 'stalker', 'church', 'cross', 'hivemind', 'domino', 'panda', 'space', 'string', 'violin', 'serenade', 'shriek', 'bear', 'robot', 'cyborg', 'nightmare', 'candle', 'sense', 'shower', 'gilles', 'deleuze', 'plato', 'shelley', 'frankenstein', 'vampire', 'rhizome', 'fungi', 'mushroom', 'bacteria', 'organism', 'virus', 'carpet', 'head', 'bright', 'blight', 'broadcast', 'skreen', 'skreener', 'logic', 'madness', 'instability', 'self', 'future', 'analog', 'seed', 'oflife', 'psycho', 'criminal', 'pills', 'politics', 'daimon', 'genius', 'moss', 'parasite', 'wood', 'aperson', 'poodle', 'voyeurism', 'exploit', 'reigns', 'grass', 'nerd', 'soap', 'towel', 'handwash', 'sickness', 'gambit', 'pillow', 'drain', 'drains', 'glass', 'spiracy', 'garden', 'evidence', 'mouse', 'echidna', 'ink', 'ofdoom', 'jazz', 'free', 'bones', 'youth', 'trick', 'voice', 'patient', 'fish', 'dead', 'philosophy', 'philosopher', 'failure', 'optimist', 'skateboard', 'spice', 'splice', 'cutie', 'dude', 'inspace', 'exhibitionist', 'shack', 'writer', 'tea', 'academic', 'bag', 'cube', 'bit', 'byte', 'mega', 'mecha', 'piece', 'fan', 'bat', 'acid', 'circuit', 'system', 'garbage', 'wolf', 'tron', 'carnival', 'ophelia', 'rot', 'crow', 'fairy', 'problems', 'goth', 'paradox', 'cow', 'cycle', 'feet', 'foot', 'kiss', 'spice', 'splice', 'mathematic', 'grave', '_as_hell', 'outtahell', 'tale', 'story', 'girlfriend', 'boyfriend', 'chad', 'bee', 'sweetie', 'seed',
realname1 = 'maria', 'jonah', 'emily', 'emile', 'hannah', 'dan', 'ryan', 'chantal', 'lydia', 'henry', 'sam'
realname2 = 'walters', 'yi', 'sun', 'rogers', 'brown', 'black', 'mcgregor', 'bell'

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
movement = ["climb", "climbs", "climbed", "climbed", "climbing"], ["crawl", "crawls", "crawled", "crawled", "crawling"], [
"crumple", "crumples", "crumpled", "crumpled", "crumpling"], ["crunch", "crunches", "crunched", "crunched", "crunching"], ["dally", "dallies", "dallied", "dallied", "dallying"], ["dance", "dances", "danced", "danced", "dancing"], ["dangle", "dangles", "dangled", "dangled", "dangling"], ["dawdle", "dawdles", "dawdled", "dawdled", "dawdling"], ["run", "runs", "ran", "run", "running"], ["twirl", "twirls", "twirled", "twirled", "twirling"], ["twist", "twists", "twisted", "twisted", "twisting"], ["gnash"], ["gnashes", "gnashed", "gnashed", "gnashing", "gnaw", "gnaws", "gnawed", "gnawed", "gnawing"]
creature = 'rabbit', 'demon', 'myself', 'my friends', 'my family', 'people', 'spirit', 'ghost', 'devil', 'fox', 'wolf', 'prey', 'predator', 'beast', 'creep', 'stalker', 'vampire', 'cannibal', 'redeemer', 'unrepentant'
about = 'the way they', 'how they', 'they', 'i think about how they',  'when they', 'where they', 'thinking about how they', 'pondering over how they', 'shuddering over the way they'
release = 'have given myself over to them', 'cower', 'prostrate myself', 'have become one with them', 'am prostrate beneath them', 'bow before them', 'die before them', 'give in to them', 'resist them', 'lose myself', 'lose myself before them', 'am misunderstood', 'release myself',
want = 'they want to', 'they desire to', 'they must', 'they long to', 'i want to', 'i desire to', 'i must', 'i long to',  
creatureaction = 'eat me', 'disembowel me', 'consume me', 'devour me', 'love me', 'writhe within me', 'writhe within my insides', 'curl up within me', 'gut me', 'climb inside my skin', 'become one with me', 'take me apart', 'become my body', 'take me whole',  
i_am = 'i am', 'i\'m', 'im', 'I AM'
punc = '.', '...'
hateL = 'hate', 'detest', 'abhor', 'loathe',
loveL = 'love', 'adore', 'cherish',
desireL = 'desire', 'want', 'lust for', 'long for'
amterrifiedofL = 'am terrified of', 'fear', 'am afraid of', 'am in terror of'
everything = 'everything', 'all the things', 
iamTheyare = 'i am', 'they are', 'i am', 'i\'m', 'im', 'I AM', 'we are', 'are we', 'we are', 'am i', 'are they', 'how can they be', 'how can i be', 'why am i', 'are they' 
personaction = 'rising', 'falling', 'moaning', 'me', 'screaming', 'running', 'fleeing', 'engaged in dance', 'dancing', 'cowering', 'sneering', 'resentful', 'repentant'
some = 'i dont care what they say', ' who cares what they think', 'there is nothing here', 'there is nothing i cant do', 'i will show them all', 'i have nothing but love and peace within me', 'do not grieve for me', 'everything is ending', 'everything is beginning', 'some call me a madman', 'they call me a madman', 'am i insane', 'i am sane', 'i am not mad', 'i am not crazy', 'they call me names'
care = 'i care for', 'i care nothing for', 'i have no regard for', 'i give no fucks about', 
others = 'others', 'them', 'those people', 'anyone', 
thinks = 'what anyone thinks', 'what they think', 'what you think', 'what others think', 'what everyone thinks', 'what people say'
platitude = '', '', '', '', '', '', '', 'we could all die tomorrow', 'every breath might be our last', 'any breath might be my last', 'for whom the bell tolls', 'do not drop me', 'do not cross me', 'i curse you', 'i put a hex on you', 'everyone will pay', 'i smile at you all', 'i am hungry' 
selfdescripadj = 'broken', 'wilted', 'roaring', 'unrelenting', 'abnormal', 'abusive', 'accomplished', 'active', 'admirable', 'adorable', 'adventurous', 'affectionate', 'afraid', 'aggravating', 'aggressive', 'agreeable', 'alcoholic', 'alert', 'alluring', 'alone', 'amazing', 'ambitious', 'amusing', 'angry', 'annoyed', 'annoying', 'anxious', 'appealing', 'appreciated', 'appreciative', 'argumentative', 'arrogant', 'artificial', 'artistic', 'ashamed', 'assertive', 'athletic', 'attentive', 'attractive', 'average', 'awake', 'awesome', 'awful', 'awkward', 'bad', 'bashful', 'beautiful', 'believable', 'big', 'bitter', 'blind', 'bold', 'bored', 'boring', 'bossy', 'brave', 'bright', 'brilliant', 'businesslike', 'busy', 'calm', 'capable', 'carefree', 'careful', 'careless', 'caring', 'casual', 'cautious', 'certain', 'charming', 'cheap', 'cheerful', 'childish', 'chubby', 'clean', 'clever', 'closed-minded', 'clumsy', 'cocky', 'cold', 'colorful', 'comfortable', 'comical', 'compassionate', 'compatible', 'competent', 'competitive', 'complaining', 'complex', 'complicated', 'compulsive', 'conceited', 'concerned', 'confident', 'confused', 'confusing', 'conscientious', 'conservative', 'considerate', 'consistent', 'constructive', 'controlling', 'controversial', 'cool', 'cooperative', 'corrupt', 'courageous', 'courteous', 'crabby', 'cranky', 'crazy', 'creative', 'critical', 'crooked', 'cruel', 'curious', 'curmudgeonly', 'cute', 'dangerous', 'daring', 'decent', 'dedicated', 'deep', 'defensive', 'delighted', 'delightful', 'demanding', 'democratic', 'dependable', 'dependent', 'depressed', 'desirable', 'determined', 'devoted', 'difficult', 'direct', 'disabled', 'disappointed', 'disgusting', 'dishonest', 'disobedient', 'disorganized', 'disrespectful', 'distinguished', 'disturbed', 'dominant', 'down-to-earth', 'dumb', 'eager', 'easygoing', 'educated', 'effective', 'efficient', 'egotistical', 'elderly', 'embarrassed', 'embarrassing', 'emotional', 'employed', 'encouraged', 'encouraging', 'energetic', 'entertaining', 'enthusiastic', 'envious', 'ethical', 'evil', 'excellent', 'exceptional', 'excited', 'exciting', 'exhausted', 'experienced', 'expressive', 'extraordinary', 'extraverted', 'fair', 'faithful', 'familiar', 'famous', 'fascinating', 'fashionable', 'fat', 'feeble', 'feminine', 'fine', 'firm', 'flexible', 'flirty', 'foolish', 'forgetful', 'forgiving', 'fortunate', 'forward', 'foxy', 'fretful', 'friendly', 'frightening', 'frustrated', 'frustrating', 'funny', 'furious', 'generous', 'gentle', 'genuine', 'gifted', 'giving', 'glad', 'glamorous', 'glamorous', 'good', 'good-for-nothing', 'good-humored', 'good-looking', 'good-natured', 'gorgeous', 'gorgeous', 'graceful', 'gracious', 'grateful', 'great', 'greedy', 'grouchy', 'grumpy', 'guilty', 'handicapped', 'handsome', 'happy', 'hard', 'hard-working', 'harmless', 'harsh', 'healthy', 'heartbroken', 'helpful', 'helpless', 'hilarious', 'homeless', 'honest', 'hopeful', 'hostile', 'hot-tempered', 'humiliated', 'humorous', 'idealistic', 'ignorant', 'ill-spoken', 'imaginative', 'immature', 'impatient', 'impolite', 'important', 'impressive', 'impulsive', 'incompetent', 'inconsiderate', 'incredible', 'incredulous', 'indecisive', 'independent', 'indulgent', 'inefficient', 'inexperienced', 'influential', 'informal', 'innocent', 'insane', 'insecure', 'insensitive', 'inspirational', 'insulting', 'intellectual', 'intelligent', 'interested', 'interesting', 'intimidating', 'involved', 'irrational', 'irresponsible', 'irritable', 'irritated', 'irritating', 'jealous', 'joyful', 'kind', 'kind-hearted', 'knowledgeable', 'laid-back', 'laughing', 'lazy', 'left-handed', 'level-headed', 'liberal', 'likeable', 'little', 'lively', 'logical', 'lonely', 'lonesome', 'loud', 'lovable', 'lovely', 'loving', 'loyal', 'lucky', 'masculine', 'materialistic', 'mature', 'mean', 'messy', 'middle-aged', 'middle-class', 'modest', 'moody', 'motherly', 'muscular', 'naive', 'narrow-minded', 'natural', 'neat', 'needy', 'negative', 'neglected', 'neighborly', 'nervous', 'nice', 'noisy', 'normal', 'nosy', 'obnoxious', 'observant', 'obsessive', 'offensive', 'old', 'old-fashioned', 'open', 'open-minded', 'opinionated', 'optimistic', 'ordinary', 'organized', 'original', 'outgoing', 'outspoken', 'outstanding', 'overrated', 'overworked', 'passionate', 'pathetic', 'patient', 'peaceful', 'perceptive', 'persistent', 'persuasive', 'philosophical', 'phony', 'plain', 'playful', 'pleasant', 'pleasant', 'pleased', 'pleasing', 'polite', 'ponderous', 'poor', 'popular', 'positive', 'possessive', 'powerful', 'practical', 'predictable', 'prejudiced', 'preoccupied', 'presentable', 'pretty', 'private', 'procrastinating', 'productive', 'professional', 'prominent', 'prompt', 'proper', 'prosperous', 'protective', 'proud', 'punctual', 'pure', 'puritanical', 'quiet', 'radical', 'rational', 'realistic', 'reasonable', 'rebellious', 'reckless', 'relaxed', 'reliable', 'religious', 'remarkable', 'resourceful', 'respectable', 'respected', 'respectful', 'responsible', 'retarded', 'rich', 'ridiculous', 'romantic', 'rough', 'rowdy', 'rude', 'rushed', 'sad', 'sarcastic', 'satisfied', 'scared', 'secure', 'seductive', 'self-assured', 'self-centered', 'self-confident', 'self-conscious', 'self-sufficient', 'self-supporting', 'selfish', 'senile', 'sensible', 'sensitive', 'sentimental', 'serious', 'sexy', 'shallow', 'short', 'short-tempered', 'shy', 'sickly', 'sincere', 'skilled', 'skillful', 'skinny', 'sleepy', 'slender', 'slim', 'sloppy', 'smart', 'snobbish', 'sociable', 'social', 'soft-spoken', 'sophisticated', 'spoiled', 'spontaneous', 'stable', 'stingy', 'straightforward', 'strange', 'strict', 'strong', 'stubborn', 'stuck-up', 'stupid', 'stylish', 'successful', 'superstitious', 'supportive', 'surprised', 'suspicious', 'sweet', 'sympathetic', 'systematic', 'talented', 'talkative', 'tall', 'temperamental', 'tense', 'terrible', 'terrific', 'thankful', 'thin', 'thinking', 'thorough', 'thoughtful', 'thoughtless', 'tiny', 'tired', 'tolerant', 'touchy', 'tough', 'traditional', 'troubled', 'trusted', 'trusting', 'trustworthy', 'truthful', 'unattractive', 'uncomfortable', 'uncreative', 'undependable', 'understandable', 'understanding', 'uneducated', 'unemployed', 'unenvious', 'unfair', 'unfaithful', 'unforgettable', 'unfriendly', 'ungraceful', 'unhappy', 'uninhibited', 'unintellectual', 'unique', 'unlucky', 'unpopular', 'unpredictable', 'unreasonable', 'unreliable', 'unstable', 'unsure', 'unsympathetic', 'unusual', 'upset', 'useful', 'vain', 'valuable', 'violent', 'violent', 'vivacious', 'warm', 'warm-hearted', 'wasteful', 'weak', 'wealthy', 'weird', 'well', 'well-adjusted', 'well-known', 'well-liked', 'well-to-do', 'wise', 'wishy-washy', 'withdrawn', 'witty', 'wonderful', 'worried', 'worthy', 'young', 'youthful'
gender = 'man', 'woman', 'person', 'boy', 'girl', 'being', 'flower', 'insect', 'citizen'
random_punc = ".", "!", "!!", "?!", "!!!!!!", "!?!?!?!!!!", "?", "!!!111oneone", " :O", " :o", " D:", "! :O", "! D:" ".", "...", ".", "...", ".", "...", ".", "...", " >_>", "o_o", " *giggles nervously*", " *shifty eyes*" ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "...", " ;)", " :D", " :)", " D:", " xD", " XD", " ^.^", " ^_^", "!", " *giggles*" "?", "?", "?", "?", "?", "?", " :o", " :O", "???", " >_>", " O_O", " o_o", ".", ".", ".", ".", ".", ".", "...", "!", "?", " :D", " :|", " :)", " >_>", " >.>", " o_o", " D:", " O_O", " -_-", " ;)", " xD", " XD", " ^_^", " ^.^", " :)))"
iama = 'i am a', 'some tell me i am a', 'im proud to be', 'my mother tells me i am a', 'my friends tell me im a', 'i want someone to tell me i\'m a', 'tell me i am a', 'daddy tells me i\'m a', 'the voices whisper', 'my secret is that i am a', 'i\'ve been told i am a', 'i wonder if i\'m a', 'i think i am a'
are = 'are', 'are become', 'have become'
doyou = 'do you love me', 'do you hate me', 'do you loathe me', 'how can i be anything other than what i am', 'how can i make the voices stop', 'is there any hope', 'is there any hope for me', 'can you be loved', 'will i die', 'will i live', 'will i be killed', 'will this world kill me', 'when will it end', 'is there any end', 'will i be loved', 'will i be saved', 'who will be saved', 'you can be saved'

sen1 = 'i wonder,'
sen2 = 'i ask you'

sen1or2 = sen1, sen2


def sentence():
    return print

holybeing = 'god', 'the devil', 'satan', 'lucifer', 'jesus christ', 'the sandman', 'angels', 'our lord', 'our lord jesus christ', 'jesus', 'our saviour', 'allah',
caredonot = 'cares for', 'does not care about', 'salivates', 'cares not for', 'has care for', 'loves', 'loathes', 'hates', 'despises', 'abhors', 'forgives', 'does not forgive', 'will not forgive', 'cannot forgive', 'curses', 'pities', 'weeps for', 'moans for', 'wants to fuck' 
forabout = 'for', 'about', 
doshouldcare = 'do you care', 'you should care' 
doomwords = 'hellfire', 'doom', 'gloom', 'plague', 'rats', 'a pox', 'disease', 'wrath', 'violence', 'repentance', 'vengeance', 
youandyour = 'you', 'your loved ones', 'your family', 'your friends', 'your neighbours', 'our families', 'our loved ones', 'our friends', 'our neighbours', 'our society', 'this society', 'these wretched beings', 'you wretched beings', 'you pathetic beings',
thosethey = 'those', 'they', 'people', 'sinners', 'citizens', 'scum', 'scumbags', 'rats', 'creeps', 'violators', 
whodoornot = 'who do', 'who do not', 'who will not', 'who'
repent = 'repent', 'lavish praise', 'pray', 'apply for salvation', 'alleviate thy sins', 'alleviate their sins', 'admit their sins', 'prostrate themselves', 'submit', 'fall on hands and knees', 'lay prone', 'submit themselves', 'sacrifice themselves', 'sacrifice', 'sacrifice their loved ones',
willfind = 'will find', 'will experience', 'find themselves', 'will fall to', 'will witness', 'will bear witness to', 'deserve', 'will suffer', 
uponthem = 'upon them', 'before them', 'before thy saviour', 
doompunc = '', '!', '!!!', '!!!!!!!!!!', '!!', '.', '...' '...!', '!!!!!!!!!!!!!!!!!!!!!!!!!', '?!?!'
pluralorno = "", "s", "es"
condemn = 'wretched', 'sinning', 'scum', 'sinner', 'devilish', 'lusting', 'lusty', 'greedy', 'selfish', 'lazy', 'gluttonous', 'lazing', 'diseased', 'despicable', 'wasting', 'pathetic', 'pitiful', 'deplorable', 'contemptible', 'straying', 'evil', 'demonic', 'wicked', 'immoral', 'straying', 'erring'
finish = ''
inwith = 'in', 'with'
rapture = 'rapture', 'ecstasy', 'terror', 'holiness', 'sanctity', 'the sacred', 'sanctitude', 'numinousness', 'blessings', 'sin', 'the holy spirit', 'light', 'angels', 'spirit', 'the spirit'
iam = ''
theyare = ''
myself = 'string = (rc(iamTheyare), rc(personaction), rc(inwith), rc(rapture) + rc(doompunc))' #change iamtheyare to iam
they = 'string = (rc(iamTheyare), rc(personaction), rc(inwith), rc(rapture) + rc(doompunc))' #change iamtheyare to they
i_others = 'i', 'the rest', 'others', 'they', 'i', 'i', 'we will not', 'we', 'you'

myselforthey = myself, they

referent = rc(holybeing)

topicList = []      #create list to store/track topics (nouns) that are pulled from lists
topicList.append(referent) #add new noun variable to topiclist to track that it has been used

#LECTICON
feel = hateL, loveL, desireL, amterrifiedofL, 
SEcare = others, thinks

print(referent  , rc(caredonot), rc(youandyour) + rc(doompunc))
print(rc(thosethey), rc(whodoornot), rc(repent), rc(uponthem), rc(willfind), rc(doomwords), "and", rc(doomwords) + rc(doompunc))
print(rc(thosethey), rc(whodoornot), rc(repent), rc(uponthem), rc(willfind), rc(doomwords), "and", rc(doomwords) + rc(doompunc))
print("")
print("i", rc(rc(feel)), rc(holybeing) + rc(pluralorno))
print(rc(i_others), rc(release) + rc(punc), rc(want), rc(creatureaction) + rc(doompunc))
print(rc(iamTheyare), rc(personaction), rc(inwith), rc(rapture) + rc(doompunc))
print("")
print(rc(doyou) + rc(doompunc))