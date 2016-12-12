import requests
import json
import datetime
import time

import redis
conn = redis.Redis('localhost')

def scrapData():
	count = 0
	while True:

		req = requests.get("https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json")
		data = req.json()

		count += 1

		setData = data
		setData["lasupdatedtime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		setData["count"] = count
		nifty50Data = json.dumps(setData)
		conn.set("nifty50Data", nifty50Data)
		conn.set("lasupdatedtime", setData["lasupdatedtime"])


		time.sleep(300)



	# print conn.hgetall(str(each.get("symbol")))