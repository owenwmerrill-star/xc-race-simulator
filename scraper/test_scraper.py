from scraper import scrape_meet
import json

meet = scrape_meet(
    "https://www.athletic.net/CrossCountry/meet/256297/info"
)

print(meet.keys())
with open("debug.json", "w") as f:
    json.dump(meet, f, indent=2)