import os
import subprocess

DATABASE_PATH = "data/xc_database.db"

print("Resetting database...")

if os.path.exists(DATABASE_PATH):
    os.remove(DATABASE_PATH)
    print("Deleted old database")
else:
    print("No existing database found")

print("Creating new database...")
subprocess.run(["python", "database/create_database.py"], check=True)

print("Database reset complete")