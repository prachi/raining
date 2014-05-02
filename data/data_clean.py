import json
from urllib2 import urlopen

def getplace(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    # print j
    country = town = None
    # print j['results']
    if j['results'] != []:
	    components = j['results'][0]['address_components']
	    for c in components:
	        if "country" in c['types']:
	            country = c['long_name']
	        if "administrative_area_level_1" in c['types']:
	            town = c['long_name']
	    return town, country
    else:
		return None, None

f = open('00.json.1','w')
with open('00.json') as fp:
	for line in fp:
		data = json.loads(line)
		if (data.has_key("created_at") & data.has_key("coordinates") & (data.get("lang") == "en") & (data.get("coordinates") != None)):
			#if data.get("entities").get("hashtags") != []:
			tags = data.get("entities").get("hashtags")
			for tag in tags:
				txt = tag.get("text")
				place = data.get("coordinates").get("coordinates")
				town, country = getplace(place[1], place[0])
				at = {"created_at": data.get("created_at")}
				dim = {	country: {town: txt} }
				met = {	"favorite_count": data.get("favorite_count"),
						"retweet_count": data.get("retweet_count") }
				f.write(json.dumps(at) + "\n")
				f.write(json.dumps(dim) + "\n")
				f.write(json.dumps(met) + "\n")

f.close()
