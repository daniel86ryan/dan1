import random


def rc(list):
    return random.choice(list)

#age = random.randint(11,68)
age = '27', '17', '13', '20', '12', '16', '14', '29', '25', '26', '23', '21', '28', '24', '18', '30', '19', '15', '22', '35', '38', '39', '29', '49', '68', '31', '59', '70', '30', '53', '27', '41', '44', '37', '33'
gender = 'm', 'f', 'nb', 'transfem', 'transmasc', 'male', 'female', 'boy', 'girl', 'man', 'woman', 'person', 'human', 'earthling', 'nonbinary', 'undetermined', 'neutral', 'androgynous'
sexpref = 'straight', 'bi', 'gay', 'lesbian', 'ace', 'asexual', 'lbgtq', 'queer', 'bisexual' 
#likes = 'rabbits', 'kittens', 'dogs', 'cute people', 'cute boys', 'cute girls', 'murder', 'psychos', 'weird stuff', 'horror movies', 'romance novels', 'kids', 'walks in the park', 'themeparks', 'books', 'space', 'aliens', 'board games', 'music', 'guitar', 'singing', 'science', 'sports', 'rain', 'summer', 'winter'
likes = 'love rabbits', 'love kittens', 'love dogs', 'love cute people', 'love cute boys', 'love cute girls', 'love murder', 'love psychos', 'love weird stuff', 'love horror movies', 'love romance novels', 'love kids', 'love walks in the park', 'love themeparks', 'love books', 'love space', 'love aliens', 'love board games', 'love music', 'love guitar', 'love singing', 'love science', 'love sports', 'love rain', 'love summer', 'love winter'
#hates = 'rabbits', 'kittens', 'dogs', 'cute people', 'cute boys', 'cute girls', 'murder', 'psychos', 'weird stuff', 'horror movies', 'romance novels', 'kids', 'walks in the park', 'themeparks', 'books', 'space', 'aliens', 'board games', 'music', 'guitar', 'singing', 'science', 'sports', 'rain', 'summer', 'winter'
hates = 'hate rabbits', 'hate kittens', 'hate dogs', 'hate cute people', 'hate cute boys', 'hate cute girls', 'hate murder', 'hate psychos', 'hate weird stuff', 'hate horror movies', 'hate romance novels', 'hate kids', 'hate walks in the park', 'hate themeparks', 'hate books', 'hate space', 'hate aliens', 'hate board games', 'hate music', 'hate guitar', 'hate singing', 'hate science', 'hate sports', 'hate rain', 'hate summer', 'hate winter'
quirk = 'love my family', 'star wars for life', 'obsessed with butter', 'pregnant af right now',


# for f in random.shuffle([a,b,c,d,e,f]):
#  f()



list1 = ([gender,sexpref, likes, quirk, hates])
random.shuffle([list1])

print("\n ABOUT ME:")

newList = []

for x in list1:
    newList.append(rc(x))

l = len(newList)
while l >=0:
    next = rc(newList)
    print(next + ".", end = ' ')
    newList.remove(next)


#print("ABOUT ME: " + rc(list1) + ". ")
#print(rc(newList))