#WQ Clock Code

import time
import os


def chime():
    
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    
    #doesn't play too early or too late
    if((hour > 6) and (hour < 21)):
        #ensure it is tolling time
        if(minute == 0):
            #adjust for 24 hour time
            if(hour > 12):
                hour = hour - 12
            
            #tolling in action
            os.system("omxplayer -o local --vol 900 MainTune.wav")
            #plays a different amount of bell tolls depending on the hour
            while(hour > 0):
                os.system("omxplayer -o local --vol 900 BellToll.wav")
                hour = hour - 1
#main loop
while(1==1):   
    chime()
    #makes sure it doesn't run more than once per hour
    time.sleep(60)
