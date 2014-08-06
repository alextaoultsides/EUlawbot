# -*- coding: utf-8 -*-

#eulawbotinbed.py
#retrieves tweet from EULAWBOT, adds "in bed!" to the end, posts to EULAWBOTINBED and laughter ensues.

import twitter
import time
api = twitter.Api(consumer_key='nope', consumer_secret='nope', access_token_key='nope', access_token_secret='nope')

for j in range(1):
    #time.sleep(300)
    
    
    
    #print api.VerifyCredentials()
    
    
    results = api.GetUserTimeline(screen_name = "EUlawbot")#Gets tweets
    
    for i in results:
        print i.GetText().encode('utf-8')
    
    print str(results[0].GetText()) + "in bed!"
    print len(str(results[0].GetText()))
    api.PostUpdate(str(results[0].GetText()) + " in bed!")
