import sqlite3

def time_to_seconds(time_string):

    if ":" in time_string:
        minutes, seconds = time_string.split(":")
        return int(minutes) * 60 + float(seconds)

    return None

def insert_meet(cursor, meet_data):
    meet = meet_data["metadata"]["meet"]

    location = meet.get("Location", {})

    course = (
        f'{location.get("Name", "")}, '
        f'{location.get("City", "")}, '
        f'{location.get("State", "")}'
    )

    cursor.execute("""
        INSERT OR IGNORE INTO meets (
            meet_id,
            name,
            date,
            course
        )
        VALUES (?, ?, ?, ?)
    """, (
        meet["ID"],
        meet["Name"],
        meet["MeetDate"],
        course
    ))

def insert_divisions(cursor, meet_data):
    for division in meet_data["division_results"]:

        # Skip divisions with no results
        if not division["results"]["resultsXC"]:
            continue

        div = division["division_info"]

        cursor.execute("""
            INSERT OR IGNORE INTO divisions (
                division_id,
                meet_id,
                name,
                gender,
                distance_meters
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            div["IDMeetDiv"],
            meet_data["metadata"]["meet"]["ID"],
            div["Division"],
            div["Gender"],
            div["Meters"]
        ))


def insert_teams(cursor, meet_data):

    for division in meet_data["division_results"]:

        # Skip divisions with no results
        results = division["results"].get("resultsXC", [])
        if not results:
            continue

        for runner in results:

            cursor.execute("""
                INSERT OR IGNORE INTO teams (
                    team_id,
                    school_name
                )
                VALUES (?, ?)
            """, (
                runner["TeamID"],
                runner["SchoolName"]
            ))

def insert_athletes(cursor, meet_data):

    for division in meet_data["division_results"]:

        # Skip divisions with no results
        results = division["results"].get("resultsXC", [])
        if not results:
            continue

        for runner in results:

            graduation_year = None

            if runner["Grade"].isdigit():
                # Cross country is in the fall, so seniors graduate the following spring
                graduation_year = (
                    meet_data["metadata"]["meet"]["SeasonID"]
                    + (13 - int(runner["Grade"]))
                )

            cursor.execute("""
                INSERT OR IGNORE INTO athletes (
                    athlete_id,
                    first_name,
                    last_name,
                    gender,
                    graduation_year,
                    team_id
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                runner["AthleteID"],
                runner["FirstName"],
                runner["LastName"],
                runner["Gender"],
                graduation_year,
                runner["TeamID"]
            ))

def insert_performances(cursor, meet_data):

    for division in meet_data["division_results"]:

        # Skip divisions with no results
        results = division["results"].get("resultsXC", [])
        if not results:
            continue

        for runner in results:

            cursor.execute("""
                INSERT OR IGNORE INTO performances (
                    result_id,
                    athlete_id,
                    division_id,
                    grade,
                    place,
                    time_seconds,
                    score,
                    official,
                    is_pr
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                runner["IDResult"],
                runner["AthleteID"],
                runner["IDDiv"],
                runner["Grade"],
                runner["Place"],
                time_to_seconds(runner["Result"]),
                runner["Score"],
                runner["Official"],
                runner["isPr"],
            ))

def insert_meet_data(meet_data):

    conn = sqlite3.connect("data/xc_database.db")
    cursor = conn.cursor()

    insert_meet(cursor, meet_data)
    insert_divisions(cursor, meet_data)
    insert_teams(cursor, meet_data)
    insert_athletes(cursor, meet_data)
    insert_performances(cursor, meet_data)

    conn.commit()
    conn.close()