def get_results_data(sb, division_id, jwt_meet):

    results = sb.execute_async_script(f"""
        const callback = arguments[arguments.length - 1];

        fetch("/api/v1/Meet/GetResultsData3", {{
            method: "POST",
            credentials: "include",
            headers: {{
                "Content-Type": "application/json",
                "Accept": "application/json, text/plain, */*",
                "anet-appinfo": "web:web:0:240",
                "anettokens": "{jwt_meet}"
            }},
            body: JSON.stringify({{
                divId: {division_id}
            }})
        }})
        .then(r => r.json())
        .then(data => callback(data))
        .catch(e => callback({{
            error: e.toString()
        }}));
    """)

    return results