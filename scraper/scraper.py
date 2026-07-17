from seleniumbase import SB

from .utils import extract_meet_id
from .fetch_meet import get_meet_data
from .fetch_results import get_results_data


def scrape_meet(url):

    meet_id = extract_meet_id(url)

    with SB(uc=True) as sb:

        # Establish browser session
        sb.open(f"https://www.athletic.net/CrossCountry/meet/{meet_id}")

        sb.sleep(4)

        metadata = get_meet_data(sb, meet_id)

        jwt_meet = metadata["jwtMeet"]

        division_results = []

        for division in metadata["xcDivisions"]:

            print(f"Downloading {division['DivName']} ({division['Gender']})")

            results = get_results_data(
                sb,
                division["IDMeetDiv"],
                jwt_meet
            )

            division_results.append({
                "division_info": division,
                "results": results
            })

        return {
            "metadata": metadata,
            "division_results": division_results
        }