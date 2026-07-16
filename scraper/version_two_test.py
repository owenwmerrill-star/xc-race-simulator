import requests
import pandas as pd

url = "https://www.athletic.net/api/v1/Meet/GetResultsData3"

# this is the "body" you send with the request
payload = {"divId": 1018811}

response = requests.post(url, json=payload)
data = response.json()

results = []
for runner in data["resultsXC"]:
    results.append({
        "place": runner["Place"],
        "first_name": runner["FirstName"],
        "last_name": runner["LastName"],
        "time": runner["Result"],
        "school": runner["SchoolName"],
        "grade": runner["Grade"],
        "gender": runner["Gender"]
    })

df = pd.DataFrame(results)
print(df.head(10))