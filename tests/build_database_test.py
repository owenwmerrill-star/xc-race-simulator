import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from scraper.scraper import scrape_meet
from database.insert import insert_meet, insert_meet_data

meet = scrape_meet(
    "https://www.athletic.net/CrossCountry/meet/256297/info"
)

insert_meet_data(meet)

print("Done!")