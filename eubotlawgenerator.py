# -*- coding: utf-8 -*-

import nltk
import twitter
import random
import re
import time

safe_tags = ['N', 'P', 'DET', 'NP','NN']#Good parts of speech to start sentences with.

#in: conditional frequency distribution, random seed word, length of senctence in words.
#out: Full sentence to be sent to Twitter.
def eu_generator(cfdist, word, num= 15):
    perc = .2 #Top 20 percent most frequent words
    rand = 0

    word = word.lower() #changes all text to lowercase
    sent = word.title() #First word starts with uppercase letter
    
    for i in range(num):
        
        percs = perc * len(cfdist[word].keys())
        
        if percs > 1 and len(sent) < 115:
            rand = random.randrange(0,int(percs))
            if len(cfdist[word].keys()[rand]):
                if re.match("^[A-Za-z_-]*$", cfdist[word].keys()[rand]):
                    word = cfdist[word].keys()[rand]
                    sent = sent + " " + word                
                else:
                    word = cfdist[word].max()
                    sent = " " + sent + " " + word
    print sent
     
    return sent
    

text = open('english.txt', 'r') #Opens European Union corpus
texts = text.read() 
tokens = nltk.word_tokenize(texts)#tokenizes the entire text.
bigrams = nltk.bigrams(tokens)  #creates unique bigrams(every two words in sequence)

cfd = nltk.ConditionalFreqDist(bigrams)#gets the frequency of each bigram in the text

rando = ""
for i in range(1):#Can change to infinite or how many sentences and tweets you would like
    
    rando = random.choice(tokens)
    
    while nltk.pos_tag(nltk.word_tokenize(rando))[0][1] not in safe_tags:#finds random word that is in the Safe tags.
        rando = random.choice(tokens)
    
    
    eubot = eu_generator(cfd, rando)
    
    if len(nltk.word_tokenize(a)) > 1:
        print eubot
        
        
        time.sleep(300)
        
        #posts to Twitter,  keys and passes are secret
        api = twitter.Api(consumer_key='nope', consumer_secret='nope', access_token_key='nope', access_token_secret='nope')
        final_sent = "Art " + str(int(random.randrange(1,5000))) + ": " + a #random fake "Article"
        api.PostUpdate(final_sent) #posted to Twitter
    
