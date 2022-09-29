import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://netbox:443/api/wireless/wireless-lan-groups/"

payload = json.dumps({
  "name": "Asia_Pacific_WLANs",
  "slug": "asia-pacific-wlans",
  "description": "Asia Pacific Wireless Networks"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': os.getenv('api_token')
}

r = requests.request("POST", url, headers=headers, data=payload)
pretty_json = json.loads(r.text)
print (json.dumps(pretty_json, indent=4))