<picture>
  <source srcset="https://github.com/user-attachments/assets/6af1ff70-3abe-4890-a952-900a18589590" media="(prefers-color-scheme: dark)">
  <img src="https://github.com/user-attachments/assets/9d9a4e42-cd46-452e-9ea8-2c03e0289006">
</picture>

---

# Streaming protocol

The Nameless Analytics Streaming protocol is a python script that sends data to [Nameless Analytics Server-side client tag](https://github.com/tommasomoretti/nameless-analytics-server-side-client-tag/).

For an overview of how Nameless Analytics works [start from here](https://github.com/tommasomoretti/nameless-analytics/).

Table of contents:
- [Required fields](#required-fields)
- [Send Streaming protocol requests ](#send-streaming-protocol-requests)



## Required fields

| **Parameter name**         | **Type** | **Field description**           |
|----------------------------|----------|---------------------------------|
| event_name                 | String   | Event name                      |
| event_date                 | String   | Event date                      |
| event_datetime             | String   | Event date and time             |
| event_timestamp            | Integer  | Event timestamp                 |
| event_origin               | String   | Event origin                    |
| client_id                  | String   | Unique client identifier        |
| session_id                 | String   | Unique session identifier       |
| event_id                   | String   | Unique event identifier         |
| page_id                    | String   | Unique page identifier          |



## Send Streaming protocol requests 
```python
# NAMELESS ANALYTICS MEASUREMENT PROTOCOL 
# PYTHON EXAMPLE CODE  
# 
# Always include in the request:
# - event_name as string
# - event_timestamp in milliseconds as integer
# - event_date as string
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
gtm_preview_header = 'ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NzdlNTU0YmM5YWY0MGJjOTQ5Yw==' # Modify this according with GTM Server-side preview header 

event_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
event_datetime = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec='microseconds')
event_timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)
processing_event_timestamp = None
event_origin = 'Measurement Protocol'
job_id = secrets.token_hex(8)
client_id = 'iURYgLE478F7TZU' # Modify this according to the current user's client_id
user_id = None # Add it if exists
session_id = 'iURYgLE478F7TZU_vh5IxJjEiYxKOhh' # Modify this according to the current user's session_id
event_name = 'purchase' # Modify this according to the event to be sent
page_id = 'A4adxB8qx2tZy' # Modify this according to the current user's page_id
event_id = f'{page_id}_{secrets.token_hex(8)}'


# --------------------------------------------------------------------------------------------------------------


# Minimum required fields
payload = {
    "event_date": event_date,
    "event_datetime": event_datetime,
    "event_timestamp": event_timestamp,
    "processing_event_timestamp": processing_event_timestamp,
    "event_origin": event_origin,
    "job_id": job_id,
    "client_id": client_id,
    "session_id": session_id,
    "event_name": event_name,
    "event_id": event_id,
    "event_data": {
        "page_id": page_id,
    },
    "user_data": {},
    "session_data": {},
}


# Recommended fields
# {
#   "user_data": {
#     "user_id": "abcd1234"
#   },
#   "event_data": {
#     "event_type": "page_view",
#     "channel_grouping": "direct",
#     "source": "direct",
#     "campaign": null,
#     "campaign_id": null,
#     "campaign_term": null,
#     "campaign_content": null,
#     "country": "IT",
#     "city": "venice",
#     "page_title": "Tommaso Moretti | Freelance digital data analyst",
#     "page_hostname_protocol": "https",
#     "page_hostname": "tommasomoretti.com",
#     "page_location": "/",
#     "page_fragment": null,
#     "page_query": null,
#     "page_extension": null,
#     "page_referrer": null,
#     "cs_container_id": "GTM-PW7349P",
#     "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
#     "browser_name": "Chrome",
#     "browser_language": "it-IT",
#     "browser_version": "135.0.0.0",
#     "device_type": "desktop",
#     "device_vendor": "Apple",
#     "device_model": "Macintosh",
#     "os_name": "Mac OS",
#     "os_version": "10.15.7",
#     "screen_size": "1512x982",
#     "viewport_size": "1512x823",
#     "page_language": "it"
#   },
#   "consent_data": { # Retrieve this information in real time calling window.get_last_consent_values() JavaScript utility function or later from BigQuery by taking it from the last event recorded on the page of the event to be sent
#     "respect_consent_mode": "Yes", # Not available when using window.get_last_consent_values(). Retrieve this information from the Nameless Analytics Client-side configuration variable tag configuration (optional).
#     "consent_type": "Update",
#     "ad_user_data": "Denied",
#     "ad_personalization": "Denied",
#     "ad_storage": "Denied",
#     "analytics_storage": "Granted",
#     "functionality_storage": "Denied",
#     "personalization_storage": "Denied",
#     "security_storage": "Denied"
#   }
# }


# Automatically added fields (do not add them manually, they will be overwritten by the server)
# {
#   "user_data": {
#     "user_date": "2025-05-04",
#     "user_timestamp": 1746342150300,
#     "user_channel_grouping": "gtm_debugger",
#     "user_source": "tagassistant.google.com",
#     "user_campaign": null,
#     "user_campaign_id": null,
#   },
#   "session_data": {
#     "session_date": "2025-05-04",
#     "session_timestamp": 1746342150300,
#     "session_channel_grouping": "gtm_debugger",
#     "session_source": "tagassistant.google.com",
#     "session_campaign": null,
#     "session_campaign_id": null
#   },
#   "event_data": {
#     "ss_hostname": "gtm.tommasomoretti.com",
#     "ss_container_id": "GTM-KQG9ZNG"
#   },
#   "client_id": "IQzbBl9NsUVV0YX",
#   "session_id": "IQzbBl9NsUVV0YX_HPUfDT84KnVV7q",
#   "processing_event_timestamp": 1746342471183,
#   "content_length": 1371
# }


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
```

---

Reach me at: [Email](mailto:hello@tommasomoretti.com) | [Website](https://tommasomoretti.com/?utm_source=github.com&utm_medium=referral&utm_campaign=nameless_analytics) | [Twitter](https://twitter.com/tommoretti88) | [Linkedin](https://www.linkedin.com/in/tommasomoretti/)
