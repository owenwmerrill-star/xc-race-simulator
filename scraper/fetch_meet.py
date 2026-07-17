def get_meet_data(sb, meet_id):

    api_url = f"/api/v1/Meet/GetMeetData?meetId={meet_id}&sport=xc"

    meet = sb.execute_async_script(f"""
        const callback = arguments[arguments.length - 1];

        fetch("{api_url}")
            .then(r => r.json())
            .then(data => callback(data))
            .catch(e => callback({{
                error: e.toString()
            }}));
    """)

    return meet