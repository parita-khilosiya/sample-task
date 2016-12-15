import requests
import json
import datetime
import time

import redis
conn = redis.Redis(host="pub-redis-13650.us-east-1-2.1.ec2.garantiadata.com", port=13650, password="redis1234")

def scrapData():
	# count = 0
	while True:
		try:    		
			req = requests.get("https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json")
			data = req.json()
			
			# count += 1

			setData = data
			setData["lasupdatedtime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			# setData["count"] = count
			nifty50Data = json.dumps(setData)
			conn.set("nifty50Data", nifty50Data)
			conn.set("lasupdatedtime", setData["lasupdatedtime"])

		except requests.exceptions.ConnectionError:
    		 print "Connection refused"

		time.sleep(300)

