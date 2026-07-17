import sqlite3

conn = sqlite3.connect("data/xc_database.db")

cursor = conn.cursor()

# make meet table
cursor.execute("""
CREATE TABLE IF NOT EXISTS meets (

    meet_id INTEGER PRIMARY KEY,

    name TEXT,

    date TEXT,

    course TEXT,

    season INTEGER
)
""")

# make divisions table - each meet has multiple divisions (e.g. boys varsity, girls varsity, boys junior varsity)
cursor.execute("""
CREATE TABLE IF NOT EXISTS divisions (

    division_id INTEGER PRIMARY KEY,

    meet_id INTEGER,

    name TEXT,

    gender TEXT,

    distance_meters INTEGER,

    FOREIGN KEY(meet_id) REFERENCES meets(meet_id)

)
""")

#makes athletes table
cursor.execute("""
CREATE TABLE IF NOT EXISTS athletes (

    athlete_id INTEGER PRIMARY KEY,

    first_name TEXT,

    last_name TEXT,

    gender TEXT,
               
    graduation_year INTEGER,

    team_id INTEGER, 
                   
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
)
""")

# makes a specfic table for teams, which will be referenced by athletes and results
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (

    team_id INTEGER PRIMARY KEY,

    school_name TEXT
)
""")


# makes a result refrencing a division (that points to a meet), athlete, and their team, including their time and place
cursor.execute("""
CREATE TABLE IF NOT EXISTS performances (

    result_id INTEGER PRIMARY KEY,

    athlete_id INTEGER,

    division_id INTEGER,

    grade TEXT,

    place INTEGER,

    time_seconds REAL,

    score INTEGER,

    official INTEGER,

    is_pr INTEGER,
               
    FOREIGN KEY(athlete_id) REFERENCES athletes(athlete_id),

    FOREIGN KEY(division_id) REFERENCES divisions(division_id)

)
""")

conn.commit()

conn.close()

print("Database created successfully!")