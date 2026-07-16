import requests
url = "https://www.athletic.net/CrossCountry/meet/217447/results/869219"
response = requests.get(url)
print("Status Code:", response.status_code) 
print(response.text[:500]) # Print the first 500 characters of the response text