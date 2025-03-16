# NAMELESS ANALYTICS MEASUREMENT PROTOCOL 
# PYTHON EXAMPLE CODE  
# 
# Always include in the request:
# - event_name: 
# - event_timestamp:
# - event_origin = 'Measurement Protocol'
# - client_id = 15 chars alphanumeric random string
# - session_id = client_id + 15 chars alphanumeric random string
# - page_id = 15 chars alphanumeric random string
# - event_id = page_id + 15 chars alphanumeric random string

import requests
import secrets
import json
from datetime import datetime, timezone


# --------------------------------------------------------------------------------------------------------------


full_endpoint = 'https://gtm.tommasomoretti.com/tm/nameless' # Modify this according to your GTM Server-side endpoint 
origin = 'https://tommasomoretti.com' # Modify this according to request origin
gtm_preview_header = 'ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NTgwZDIzMDZmNGY0ZDEwZmM2Mg==' # Modify this according with GTM Server-side preview header 

event_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
event_datetime = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec='microseconds')
event_timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)
processing_event_timestamp = None
event_origin = 'Measurement Protocol'
job_id = secrets.token_hex(8)
client_id = '005cKxwvVDPMjG3' # Modify this according to the current user's client_id
user_id = None # Add it if exists
session_id = '005cKxwvVDPMjG3_kbNdatKCaN4EWb' # Modify this according to the current user's session_id
event_name = 'purchase' # Modify this according to the event to be sent
page_id = 'q4adxB8qx2toy' # Modify this according to the current user's page_id
event_id = f'{page_id}_{secrets.token_hex(8)}'

# Retrieve this information in real time calling window.get_last_consent_values() JavaScript utility function or later from BigQuery by taking it from the last event recorded on the page of the event to be sent
respect_consent_mode = "No" # Not available when using window.get_last_consent_values(). Retrieve this information from the Nameless Analytics Client-side configuration variable tag configuration (optional).
tracking_anonimization = "No" #  Not available when using window.get_last_consent_values(). Retrieve this information from the Nameless Analytics Client-side configuration variable tag configuration (optional).
consent_type = "Update"
ad_user_data = "Granted"
ad_personalization = "Denied"
ad_storage = "Granted"
analytics_storage = "Granted"
functionality_storage = "Granted"
personalization_storage = "Granted"
security_storage = "Granted"

payload = {
    "event_date": event_date,
    "event_datetime": event_datetime,
    "event_timestamp": event_timestamp,
    "processing_event_timestamp": processing_event_timestamp,
    "event_origin": event_origin,
    "job_id": job_id,
    "client_id": client_id,
    "user_id": user_id,
    "session_id": session_id,
    "event_name": event_name,
    "event_data": {
        "page_id": page_id,
        "event_id": event_id
    },
    "consent_data": {
        "respect_consent_mode": respect_consent_mode,
        "tracking_anonimization": tracking_anonimization,
        "consent_type": consent_type,
        "ad_user_data": ad_user_data,
        "ad_personalization": ad_personalization,
        "ad_storage": ad_storage,
        "analytics_storage": analytics_storage,
        "functionality_storage": functionality_storage,
        "personalization_storage": personalization_storage,
        "security_storage": security_storage
    }
}

print("----- NAMELESS ANALYTICS -----")
print("--------- DATA LOADER --------")
print("Function execution start: 🤞")
print('👉 Send request to ' + full_endpoint)

headers = {
    'Content-Type': 'application/json',
    'Origin': origin,
    'X-Gtm-Server-Preview': gtm_preview_header,
}

try:
    response = requests.post(full_endpoint, json=payload, headers=headers)
    response.raise_for_status()
    response_json = response.json()
    
    if "response" in response_json:
        response_json["response"] = bytes(response_json["response"], "latin1").decode("utf-8")

    print(" ", response_json.get("response"))
    
    response_data = json.dumps(response_json.get("data", "No data"), indent=2, ensure_ascii=False)
    indented_response = "\n".join(["  " + line for line in response_data.splitlines()])
    print("  👉 Request response: ")
    print(indented_response)
    print("Function execution end: 👍")


except requests.exceptions.RequestException as e:
    try:
        error_response = e.response.json()
        if "response" in error_response:
            error_response["response"] = bytes(error_response["response"], "latin1").decode("utf-8")
        print("  ", error_response.get("response", "No data"))
        raise 
    except:
        print('🔴 Request failed:', str(e))