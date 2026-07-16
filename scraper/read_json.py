import json

# Open the JSON file
with open("data/raw/meet_256297.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print()

print("\n=== Teams ===")
print(data["teams"])

print("\n=== Team Scores ===")
print(data["teamScores"])

print()
print(data["teams"][0])