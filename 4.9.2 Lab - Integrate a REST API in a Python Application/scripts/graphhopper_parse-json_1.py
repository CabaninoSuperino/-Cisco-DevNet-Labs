import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "c29ff1ee-7a4c-4e41-bde1-83aef92d6fc0"

url = geocode_url + urllib.parse.urlencode({"q": loc1, "limit": "1", "key": key})
replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code
print(json_data)