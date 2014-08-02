# -*- coding: utf-8 -*-

import twitter
import time
api = twitter.Api(consumer_key='nope', consumer_secret='nope', access_token_key='nope', access_token_secret='nope')

for j in range(1):
    #time.sleep(300)
    
    
    
    #print api.VerifyCredentials()
    
    
    results = api.GetUserTimeline(screen_name = "EUlawbot")
    
    for i in results:
        print i.GetText().encode('utf-8')
    
    print str(results[0].GetText()) + "in bed!"
    print len(str(results[0].GetText()))
    api.PostUpdate(str(results[0].GetText()) + " in bed!")
