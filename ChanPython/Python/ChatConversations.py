


CHAT CONVERSATIONS

"" ''

### Opinions

Question = What do you think about (topic)?

   "A(PC doesn't like it and they do)1: Ah, too bad, I love (topic)!"
        GMS>>> ah + ", " + too_bad + " " + I + " " + love + " " + (topic) + excl_punc

    "A(PC doesn't like it and they do)2: Really? How can you not like (topic)? I am obsessed with (topic)."
        GMS>>> Really + "? " How_can_you_not_like + " " + topic + quest_punc + " " + I + " " + am_obsessed_with + " " + topic + ".” 

   "A(PC doesn't like it and they do)3: I'll never understand how someone can't like (topic). It's so interesting!"
        GMS>>> I_will + " " + never + " how " + someone + " " + cant + " " + like + TOPIC + ". " + it_is + " " + so + " " + interesting + ".” 
	    #[[[GRAMMAR: if TOPIC ends in ‘s', change it_is to they_are. exceptions like: chess]]]

    "A(PC doesn't like it and they do)4: Eugh, (topic) gives me the shivers."
        GMS>>> eugh + ", " + " " + TOPIC + " " + freaks_me_out_casual + period_nervous


A (PC likes it and they do)1: Yes! I love (topic) too!
A (PC likes it and they do)2: I knew I liked you! I can't get enough of (topic).
A (PC likes it and they do)3: So you have good taste. I also love (topic).

A (PC likes it and they don't)1: I can't agree, I think (topic) sucks.
A (PC likes it and they don't)2: How can you like (topic)? Blech.
A (PC likes it and they don't)3: I don't understand how people can like (topic). Maybe one day I'll get it.

A (PC doesn't like it and they don't like it)1: See, you get it. (topic) sucks! Sometimes I feel like I'm the only one who feels this way.
 A (PC doesn't like it and they don't like it)2: Yes! (topic) is the worst! You understand me.
A (PC doesn't like it and they don't like it)3: I don't like (topic) either. It baffles me how anyone can like (topic), honestly.


str = c.hello + " " + c.PC_or_TermOfAffection + ", " + c.I + " " + c.spoke + " with " + o.username + " " + c.about + " " + c.arr_opinions[0][1][0] + ".";

———————————

Situations

example:
<touchmy> i was hanging out last night and got [caught in the rain!]>
<brightblink> that sucks
<touchmy> what! i love getting [caught in the rain!]

Statement: 

"i was hanging out last night and [got caught in the rain]"

I + " was " + hanging_out +  " " + and + " " situation_phrase


i was browsing the internet last night and found a website about [website_description: stalking]

i was looking at pictures [yesterday] and found one of [pic_description: a headless flower]

i was [with my friend] [last night] and they [verb_friend_tried_to] tried to wrestle with me]




> EXPRESS PLEASURE
> EXPRESS DISAPPOINTMENT

———————————————————————

Asking Advice


example: 
<touchmy> soooo gloomyeyes asked me out. you know them right? what do you think? should i say yes?
<brightblink> go for it!
<touchmy> i just have a feeling they're not right for me. i don't know about your advice giving, brightblink :\


Statement:

sooo [username] asked me out. you know them right? what do you think? should i say yes?

i got this job offer to be a [postal worker]. think i should go for it?

i'm thinking of getting into a routine of [verb - working out]. change my life up. what do you think?

i'm thinking of going to university to study [subject_intellectual]. what are your thoughts?

my friend/username invited me to a protest against [subject]. think i should attend?

my friend/username keeps encouraging me to donate to this charity that supports [subject]. what do you think? 





> ENCOURAGE THEM
> DISCOURAGE THEM


———————————————

RANDOM CHITCHAT


Do you think, if you had to, you could build a door?

Do you think there's a real meaning to life?

Why do people do things like [naughtything: cocaine]?

Do you believe in [mysteriousthing]?
mysteriousthing: ghosts, spirits, angels, demons, devils, the Devil, God, Lucifer, zombies, etc

Do you think we'll live long happy lives?


———————————————

CONVERSATIONS REFLECTING THEIR STATS:
#these should communicate to the player what stats they're high in

Intuition: "Sometimes I can just tell things are going to happen. That ever happen to you?"


Performance: "I just love to show off for other people. I don't know why, it's been like this ever since I was young."


Know-How: "I lovvve learning new things. I can never get enough. How about you?"


Serendipity: "I swear lucky things just seem to happen to me all the time. It's crazy! Do you feel that way?"


Humanity: "I love people. I love the world. Sometimes I want to give everything a hug. Do you ever get that impulse?"


