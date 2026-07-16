import requests
import json

url = "https://www.athletic.net/api/v1/Meet/GetResultsData3"

payload = {
    "divId": 1018811
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.text[:500])