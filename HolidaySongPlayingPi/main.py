#Holiday Cheer Pi

import time
import os
import random

def playSong():
	
	minute = time.localtime().tm_min
	rando = random.randint(1,3)
	
	if(minute%5 == 0):
	#random song selection, ideal for a small amount of songs
		if(rando == 1):
			os.system("omxplayer -o local --vol 900 Song1.wav")
		elif(rando == 2):
			os.system("omxplayer -o local --vol 900 Song2.wav")
		else:
			os.system("omxplayer -o local --vol 900 Song3.wav")

#main loop
while(1==1):
	playSong()
	
