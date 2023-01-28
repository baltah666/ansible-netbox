import requests
import json

url = "http://192.168.174.157:8000/api/dcim/devices/"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
