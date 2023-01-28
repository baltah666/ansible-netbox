import requests
import json

url = "http://192.168.174.157:8000/api/dcim/device-roles"

payload = "[\r\n    {\r\n        \"name\": \"WAN Router\",\r\n        \"slug\": \"wan-router\"\r\n\t\t\"color\": \"327fa8\",\r\n\t\t\"vm_role\":false\r\n    },\r\n     {\r\n        \"name\": \"Access Switch\",\r\n        \"slug\": \"access-switch\",\r\n\t\t\"color\": \"32a871\",\r\n\t\t\"vm_role\":false\r\n    },\r\n    {\r\n        \"name\": \"Wireless AP\",\r\n        \"slug\": \"wireless-ap\",\r\n\t\t\"color\": \"a86332\",\r\n\t\t\"vm_role\":false\r\n    },\r\n    {\r\n        \"name\": \"Patch Panel\",\r\n        \"slug\": \"patch-panel\",\r\n\t\t\"color\": \"dbc230\",\r\n\t\t\"vm_role\":false\r\n    }\r\n]"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
