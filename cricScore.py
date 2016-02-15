# A python script to notify Live score by scraping data from Cricinfo's RSS Feed 

import requests
import bs4
import pynotify
from time import sleep

url = "http://static.cricinfo.com/rss/livescores.xml"

def display(title,body):
	
	if pynotify.init('Test') == True:
		n = pynotify.Notification(title,body)
		n.show()



while True:

	res = requests.get(url)
	res.raise_for_status()
	#print(res.text)

	if res.status_code == requests.codes.ok:
		soupData  = bs4.BeautifulSoup(res.text,"lxml")

		scoreList = soupData.select('title')
		#scoreList is list of all  live scores 

		#print(score[1].getText())
		
		score = scoreList[1].getText() 
		# change list index depending on the match you want the notifications for

		display("Live Score",score)
		
		sleep(300)
		#notify score after an interval of 300 seconds
