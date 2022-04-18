
import random
import SortedPersonDescriptors
import GeneralAdjectiveList
import nounlist
import verbs_dictionaries
import split_tense
import WIP_poemnounadj
import shortPoem3resultsList

################################positiVe

### philosophy is <eye-opening>
### philosophy <stimulates the mind and soul>
### i love how <decadent> the Baroque period was
### i love philosophy. why? because it opens my eyes to things i didn't understand before

### consider how to account for both phrasings
### consider accounting for lecticons
### consider accounting for tense


def rc(list):
    return random.choice(list)


topic = 'philosophy', 'history', 'literature', 'the state of the world', 'the state of society', 'Parisian aesthetics', 'the Baroque period', 'the post-minimalist movement', 'biology', 'academic discourse', 'feminism', 'revolution', 'war history', 'poetry', 'geography', 'astronomy'

#intellectualDictP = 
philosophyDictP = 'stimulating', 'enlightening', 'intellectual', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'growth-inducing', 'horizon broadening', 
historyDictP = 'stimulating', 'enlightening', 'intellectual', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'rich', 'grounding', 'perspective-giving', 'horizon broadening', 'full of fascinating stories', 'the tale of our times', 'the tales of our species', 'the stories of our lives', 'the legend of our past',
literatureDictP = 'stimulating', 'enlightening', 'intellectual', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'rich', 'grounding', 'perspective-giving', 'horizon broadening', 'creative', 'real', 'authentic', 'enriching', 'moving'
the_state_of_the_worldDictP = 'intriguing', 'hopeful', 'rapidly expanding', 'on the upswing', 'better than ever', 'full of hope', 'getting better every day', 'better than before', 'better than it used to be', 'exciting', 'wild', 'crazy', 
the_state_of_societyDictP = 'intriguing', 'hopeful', 'rapidly expanding', 'on the upswing', 'better than ever', 'full of hope', 'getting better every day', 'better than before', 'better than it used to be', 'exciting', 'wild', 'crazy', 
Parisian_aestheticsDictP = 'beautiful', 'enriching', 'decadent', 'Baroque', 'luxurious', 'intense', 'vibrant', 'colourful', 'sexy', 'appealing', 'beautiful', 'complex', 'distinct',
the_Baroque_periodDictP = 'beautiful', 'enriching', 'decadent', 'luxurious', 'intense', 'vibrant', 'colourful', 'sexy', 'appealing', 'beautiful', 'complex', 'distinct',
the_postminimalist_movementDictP = 'emergent', 'modern', 'creative', 'what the world needed', 'a feat', 'striking', 'thought-provoking', 'what the doctor ordered'
biologyDictP = 'needed', 'required', 'enlightening', 'important', 'fascinating', 'stimulating', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'horizon broadening', 'educational',
academic_discourseDictP = 'needed', 'inspiring', 'enlightening', 'required', 'important', 'fascinating', 'stimulating', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'horizon broadening', 'educational', 'exciting', 'rich', 'liberation', 'for progressing humanity', 'grounding'
feminismDictP = 'needed', 'enlightening', 'the bare minimum', 'so important', 'eye-opening', 'required', 'what the world needed', 'thought-provoking', 'grounding', 'a perspective shift', 'a win for women', 'a win for everyone', 'egalitarianism', 'a step forward for humanity', 'hope', 'liberation'
revolutionDictP = 'needed', 'the bare minimum', 'so important', 'eye-opening', 'required', 'what the world needed', 'thought-provoking', 'grounding', 'a perspective shift', 'a win for everyone', 'egalitarian', 'egalitarianism', 'a step forward for humanity', 'hope', 'upheaval', 'a rearrangement of the status quo', 'a seizure for the people', 'for the little guys', 'victory', 'near', 'possible', 'wonderful', 'the idea of a better life', 'taking what is ours'
war_historyDictP = 'stimulating', 'intellectual', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'rich', 'grounding', 'perspective-giving', 'horizon broadening', 'bloodthirsty', 'full of interesting stories',
poetryDictP = 'stimulating', 'enlightening', 'intellectual', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'rich', 'grounding', 'perspective-giving', 'horizon broadening', 'creative', 'real', 'authentic', 'enriching', 'moving', 'life', 'life-changing', 'world-shaking', 'limitless potential', 'giving life to new concepts', 
geographyDictP = 'stimulating', 'intellectual', 'mind-expanding', 'eye-opening', 'mind-boggling', 'exciting', 'rich', 'grounding', 'perspective-giving', 'horizon broadening', 'full of fascinating stories', 'educational', 'educative'
astronomyDictP = 'overwhelming', 'beautiful', 'enlightening', 'a reminder of how small we are', 

myDictP = {'philosophy': philosophyDictP, 'history': historyDictP, 'literature': literatureDictP, 'biology':biologyDictP, 'academic discourse':academic_discourseDictP, 'the state of the world': the_state_of_the_worldDictP, 'the state of society':the_state_of_societyDictP, 'Parisian aesthetics':Parisian_aestheticsDictP, 'the Baroque period':the_Baroque_periodDictP, 'the post-minimalist movement':the_postminimalist_movementDictP, 'feminism':feminismDictP, 'revolution': revolutionDictP, 'poetry': poetryDictP, 'geography': geographyDictP, 'astronomy': astronomyDictP}
#myDictNegative = {'vampire': vampireDictNeg, 'teeth':teethDictNeg, 'human':humanDictNeg,'cannibal':cannibalDictNeg}


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

thistopic = rc(topic)


print('i love ' + thistopic)
print("why? because it's " + rc(myDictP[thistopic]), "and", rc(myDictP[thistopic]))
print("and I am", rc(ppadj) + ",")
print(rc(verbing), "down the " + rc(pnoun) + ",")
print(rc(verbing) + ", " + rc(verbing) + ",")
print(rc(ppadj))


# biopoliticsDictP = 
# debateDictP = 
# English_literatureDictP = 
# foreign_literatureDictP = 
# experimental_filmsDictP = 
# foreign_filmsDictP = 
# physicsDictP = 
# Japanese_literatureDictP = 
# world_geographyDictP = 
# Shakespearean_theatreDictP = 
# organised_religionDictP = 
# geneaologyDictP = 
# classicsDictP = 
# anthropologyDictP = 
# mathematicsDictP =

# subject_nature_

# natureDictP = 
# compostingDictP = 
# horticultureDictP = 
# environmentalismDictP = 
# conservation_biologyDictP = 
# entomologyDictP = 
# forestsDictP = 
# lakesDictP = 
# gemstonesDictP = 
# parasitesDictP = 
# poisonous_plantsDictP = 
# nature_documentariesDictP = 
# the_Mariana_trenchDictP = 
# mushroomsDictP = 
# fungiDictP = 
# lichenDictP = 
# moss =

# subject_animals_

# animalsDictP = 
# catsDictP = 
# animalsDictP = 
# dogsDictP = 
# birdsDictP = 
# bunniesDictP = 
# rabbitsDictP = 
# insectsDictP = 
# antsDictP = 
# bugsDictP = 
# frogsDictP = 
# beesDictP = 
# cockroachesDictP = 
# spidersDictP = 
# snakesDictP = 
# warmblooded_animalsDictP = 
# coldblooded_animalsDictP = 
# baleen_whalesDictP = 
# orcasDictP = 
# squidDictP = 
# octopuses_(yes',_'octopuses',_'not_octopi!)
# ,

# subject_technology_

# technologyDictP = 
# electronicsDictP = 
# circuitryDictP = 
# roboticsDictP = 
# technologyDictP = 
# the_internetDictP = 
# artificial_intelligenceDictP = 
# boatsDictP = 
# the_TitanicDictP = 
# classic_carsDictP = 
# weaponsDictP = 
# science_fictionDictP = 
# spaceDictP = 
# space_travelDictP = 
# robotsDictP = 
# cyborgs
# ,

# subject_creativity_

# creativtyDictP = 
# photographyDictP = 
# writingDictP = 
# readingDictP = 
# drawingDictP = 
# artDictP = 
# illustrationDictP = 
# superhero_comicsDictP = 
# paintingDictP = 
# fantasyDictP = 
# cookingDictP = 
# bookbindingDictP = 
# novelwritingDictP = 
# flashfiction_writingDictP = 
# architectureDictP = 
# carpentryDictP = 
# filmmakingDictP = 
# weaving
# ,

# subject_spirituality_

# spiritualityDictP = 
# ChristmasDictP = 
# paganismDictP = 
# shamanismDictP = 
# SamhainDictP = 
# vodounDictP = 
# goats_without_hornsDictP = 
# witchcraftDictP = 
# the_churchDictP = 
# ChristianityDictP = 
# astrologyDictP = 
# veganismDictP = 
# BuddhismDictP = 
# DruidryDictP = 
# AstrozorianismDictP = 
# RastafarianismDictP = 
# spiritualismDictP = 
# communesDictP = 
# dreams
# ,

# subject_banal_

# banalDictP = 
# marriageDictP = 
# divorceDictP = 
# romanceDictP = 
# romance_novelsDictP = 
# true_crimeDictP = 
# armchair_philosophisingDictP = 
# old_moviesDictP = 
# chessDictP = 
# ventriloquismDictP = 
# puppetsDictP = 
# board_gamesDictP = 
# sportsDictP = 
# birthdaysDictP = 
# video_gamesDictP = 
# tabletop_roleplaying_gamesDictP = 
# soccerDictP = 
# footballDictP = 
# tennisDictP = 
# exotic_danceDictP = 
# card_gamesDictP = 
# gin_rummyDictP = 
# high_fashionDictP = 
# sexDictP = 
# sexualityDictP = 
# romanceDictP = 
# relationshipsDictP = 
# loveDictP = 
# arranged_marriageDictP = 
# gamblingDictP = 
# pokerDictP = 
# strip_pokerDictP = 
# diceDictP = 
# knockknock_jokesDictP = 
# LatviaDictP = 
# feetDictP = 
# the_newsDictP = 
# the_weatherDictP = 
# rainbowsDictP = 
# campingDictP = 
# puppetsDictP = 
# dollsDictP = 
# porcelain_dollsDictP = 
# root_vegetablesDictP = 
# bootlickingDictP = 
# deep_thoughtsDictP = 
# Dark_HoleDictP = 
# modern_medicineDictP = 
# traditional_medicine
# ,

# subject_weirdandstrange_

# weirdandstrangeDictP = 
# horrorDictP = 
# ouija_boardsDictP = 
# weird_moviesDictP = 
# weird_thingsDictP = 
# high_strangenessDictP = 
# psychedelicsDictP = 
# folkloreDictP = 
# mythologyDictP = 
# urban_legendsDictP = 
# cryptozoologyDictP = 
# the_gothicDictP = 
# the_supernaturalDictP = 
# the_differences_in_animal_fleshDictP = 
# the_softness_of_hairDictP = 
# leechesDictP = 
# teethDictP = 
# tarotDictP = 
# poisonsDictP = 
# graveyardsDictP = 
# Edgar_Allan_PoeDictP = 
# freaksDictP = 
# mutantsDictP = 
# skeletonsDictP = 
# cultsDictP = 
# vampiresDictP = 
# angelsDictP = 
# zombiesDictP = 
# cultsDictP = 
# hunting_cryptidsDictP = 
# ghost_huntingDictP = 
# seancesDictP = 
# ritualsDictP = 
# magicDictP = 
# demonsDictP = 
# the_devil
# ,

# spook_type_

# spook_typeDictP = 
# ghostDictP = 
# demonDictP = 
# spiritDictP = 
# devilDictP = 
# phantomDictP = 
# bansheeDictP = 
# creepy_demon_childDictP = 
# zombieDictP = 
# vampireDictP = 
# werewolf




# #######################################NEGATIVE

# intellectualDictN = 
# philosophyDictN = 'daunting', 'boring', 'mind-boggling', 'pointless', 'dumb', 'pretentious'
# historyDictN = 
# literatureDictN = 
# the_state_of_the_worldDictN = 
# the_state_of_societyDictN = 
# Parisian_aestheticsDictN = 
# the_Baroque_periodDictN = 
# the_postminimalist_movementDictN = 
# biologyDictN = 
# academic_discourseDictN = 
# feminismDictN = 
# revolutionDictN = 
# war_historyDictN = 
# poetryDictN = 
# geographyDictN = 
# astronomyDictN = 
# biopoliticsDictN = 
# debateDictN = 
# English_literatureDictN = 
# foreign_literatureDictN = 
# experimental_filmsDictN = 
# foreign_filmsDictN = 
# physicsDictN = 
# Japanese_literatureDictN = 
# world_geographyDictN = 
# Shakespearean_theatreDictN = 
# organised_religionDictN = 
# geneaologyDictN = 
# classicsDictN = 
# anthropologyDictN = 
# mathematicsDictN =

# subject_nature_

# natureDictN = 
# compostingDictN = 
# horticultureDictN = 
# environmentalismDictN = 
# conservation_biologyDictN = 
# entomologyDictN = 
# forestsDictN = 
# lakesDictN = 
# gemstonesDictN = 
# parasitesDictN = 
# poisonous_plantsDictN = 
# nature_documentariesDictN = 
# the_Mariana_trenchDictN = 
# mushroomsDictN = 
# fungiDictN = 
# lichenDictN = 
# moss
# ,

# subject_animals_

# animalsDictN = 
# catsDictN = 
# animalsDictN = 
# dogsDictN = 
# birdsDictN = 
# bunniesDictN = 
# rabbitsDictN = 
# insectsDictN = 
# antsDictN = 
# bugsDictN = 
# frogsDictN = 
# beesDictN = 
# cockroachesDictN = 
# spidersDictN = 
# snakesDictN = 
# warmblooded_animalsDictN = 
# coldblooded_animalsDictN = 
# baleen_whalesDictN = 
# orcasDictN = 
# squidDictN = 
# octopuses_(yes',_'octopuses',_'not_octopi!)
# ,

# subject_technology_

# technologyDictN = 
# electronicsDictN = 
# circuitryDictN = 
# roboticsDictN = 
# technologyDictN = 
# the_internetDictN = 
# artificial_intelligenceDictN = 
# boatsDictN = 
# the_TitanicDictN = 
# classic_carsDictN = 
# weaponsDictN = 
# science_fictionDictN = 
# spaceDictN = 
# space_travelDictN = 
# robotsDictN = 
# cyborgs
# ,

# subject_creativity_

# creativtyDictN = 
# photographyDictN = 
# writingDictN = 
# readingDictN = 
# drawingDictN = 
# artDictN = 
# illustrationDictN = 
# superhero_comicsDictN = 
# paintingDictN = 
# fantasyDictN = 
# cookingDictN = 
# bookbindingDictN = 
# novelwritingDictN = 
# flashfiction_writingDictN = 
# architectureDictN = 
# carpentryDictN = 
# filmmakingDictN = 
# weaving
# ,

# subject_spirituality_

# spiritualityDictN = 
# ChristmasDictN = 
# paganismDictN = 
# shamanismDictN = 
# SamhainDictN = 
# vodounDictN = 
# goats_without_hornsDictN = 
# witchcraftDictN = 
# the_churchDictN = 
# ChristianityDictN = 
# astrologyDictN = 
# veganismDictN = 
# BuddhismDictN = 
# DruidryDictN = 
# AstrozorianismDictN = 
# RastafarianismDictN = 
# spiritualismDictN = 
# communesDictN = 
# dreams
# ,

# subject_banal_

# banalDictN = 
# marriageDictN = 
# divorceDictN = 
# romanceDictN = 
# romance_novelsDictN = 
# true_crimeDictN = 
# armchair_philosophisingDictN = 
# old_moviesDictN = 
# chessDictN = 
# ventriloquismDictN = 
# puppetsDictN = 
# board_gamesDictN = 
# sportsDictN = 
# birthdaysDictN = 
# video_gamesDictN = 
# tabletop_roleplaying_gamesDictN = 
# soccerDictN = 
# footballDictN = 
# tennisDictN = 
# exotic_danceDictN = 
# card_gamesDictN = 
# gin_rummyDictN = 
# high_fashionDictN = 
# sexDictN = 
# sexualityDictN = 
# romanceDictN = 
# relationshipsDictN = 
# loveDictN = 
# arranged_marriageDictN = 
# gamblingDictN = 
# pokerDictN = 
# strip_pokerDictN = 
# diceDictN = 
# knockknock_jokesDictN = 
# LatviaDictN = 
# feetDictN = 
# the_newsDictN = 
# the_weatherDictN = 
# rainbowsDictN = 
# campingDictN = 
# puppetsDictN = 
# dollsDictN = 
# porcelain_dollsDictN = 
# root_vegetablesDictN = 
# bootlickingDictN = 
# deep_thoughtsDictN = 
# Dark_HoleDictN = 
# modern_medicineDictN = 
# traditional_medicine
# ,

# subject_weirdandstrange_

# weirdandstrangeDictN = 
# horrorDictN = 
# ouija_boardsDictN = 
# weird_moviesDictN = 
# weird_thingsDictN = 
# high_strangenessDictN = 
# psychedelicsDictN = 
# folkloreDictN = 
# mythologyDictN = 
# urban_legendsDictN = 
# cryptozoologyDictN = 
# the_gothicDictN = 
# the_supernaturalDictN = 
# the_differences_in_animal_fleshDictN = 
# the_softness_of_hairDictN = 
# leechesDictN = 
# teethDictN = 
# tarotDictN = 
# poisonsDictN = 
# graveyardsDictN = 
# Edgar_Allan_PoeDictN = 
# freaksDictN = 
# mutantsDictN = 
# skeletonsDictN = 
# cultsDictN = 
# vampiresDictN = 
# angelsDictN = 
# zombiesDictN = 
# cultsDictN = 
# hunting_cryptidsDictN = 
# ghost_huntingDictN = 
# seancesDictN = 
# ritualsDictN = 
# magicDictN = 
# demonsDictN = 
# the_devil
# ,

# spook_type_

# spook_typeDictN = 
# ghostDictN = 
# demonDictN = 
# spiritDictN = 
# devilDictN = 
# phantomDictN = 
# bansheeDictN = 
# creepy_demon_childDictN = 
# zombieDictN = 
# vampireDictN = 
# werewolf