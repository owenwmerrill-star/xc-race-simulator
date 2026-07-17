import sqlite3

conn = sqlite3.connect("data/xc_database.db")
cursor = conn.cursor()

tables = ["meets", "divisions", "teams", "athletes", "performances"]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"{table:12}: {cursor.fetchone()[0]}")

conn.close()