import json
import urllib2
dom= raw_input('enter domain or company name')
url = "https://api.hunter.io/v2/domain-search?domain="+dom+"&api_key=enter_ur_API_Key&limit=100&offset=0"
response = urllib2.urlopen(url)
dataa = response.read()
valuess = json.loads(dataa)

# the result is a Python dictionary:
#print(valuess["data"]["emails"]["0:"]["value"])


a=len((valuess["data"]["emails"]))
for i in range(a):
	print(valuess["data"]["emails"][i]["value"])
	i+=1
		
