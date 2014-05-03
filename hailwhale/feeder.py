import unittest, urllib, json, time
from collections import defaultdict
from whale import maybe_dumps
import os


with open(os.path.join('Users/guest-admin/Desktop/raining/data/','data.json')) as fp:
	for line in fp:
		data = json.loads(line)
		if data.has_key("at"):
			at = data.get("at")
		if data.has_key("dim"):
			dimensions = data.get("dim")
		if data.has_key("met"):
			metrics = data.get("met")

		if (at != None) & (dimensions != None) & (metrics != None):
			print at
			print dimensions
			print metrics
			Whale.count_now('twitter', dimensions, metrics , at)
			at = None 
			dimensions = None
			metrics = None


		

