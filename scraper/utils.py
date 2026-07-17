import re

def extract_meet_id(url):
    match = re.search(r"meet/(\d+)", url)

    if not match:
        raise ValueError(f"Could not find meet ID in: {url}")

    return int(match.group(1))