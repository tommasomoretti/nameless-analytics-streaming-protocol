![Na logo beta](https://github.com/tommasomoretti/nameless-analytics/assets/29273232/7d4ded5e-4b79-46a2-b089-03997724fd10)

---

# Measurament protocol
## Required fields

| Field name                | Example value | Description                 |
|-----------------|---------------|---------------------------------------|
| event_origin    | Yes           | Measurament Protocol                  |
| event_date      | 2024-01-01    | Event date                            |
| event_name      | purchase      | Event name (do not use get_user_data) |
| event_timestamp | 1722607958646 | Event timestamp in milliseconds       |
| client_id       | | |
| session_id      | | |
| page_id         | | |
| event_id        | | |

## Send Measurement Protocol requests via Terminal
```bash
### Request configurations 
full_endpoint="https://gtm.tommasomoretti.com/tm/nameless"
origin="https://tommasomoretti.com"
gtm_preview_header="ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NTgwNWE0MDgxMzEyYjE5Mjg2Nw=="

### Request payload required fields
event_date=$(date +%Y-%m-%d)
event_datetime=$(date -u +"%Y-%m-%dT%H:%M:%S.%3N000")
event_timestamp=$(date -u +%s)000
processing_event_timestamp="null"
event_origin="Measurement Protocol"
job_id="1234"
client_id="005cKxwvVDPMjG3" # Modify this according to the current user's client_id
user_id="null" # Add it if exists
user_log="Same user, same session"
session_id="005cKxwvVDPMjG3_kbNdatKCaN4EWb" # Modify this according to the current user's session_id
event_name="purchase" # Modify this according to the event to be sent
page_id="q4adxB8qx2toy" # Modify this according to the current user's page_id
event_id="${page_id}_$(openssl rand -hex 6)"

### JSON Payload
payload=$(cat <<EOF
{
  "event_date": "$event_date",
  "event_datetime": "$event_datetime",
  "event_timestamp": "$event_timestamp",
  "processing_event_timestamp": $processing_event_timestamp,
  "event_origin": "$event_origin",
  "job_id": "$job_id",
  "client_id": "$client_id",
  "user_id": $user_id,
  "user_log": "$user_log",
  "session_id": "$session_id",
  "event_name": "$event_name",
  "event_data": {
    "page_id": "$page_id",
    "event_id": "$event_id"
  }
}
EOF
)

### Send Request
curl -X POST "$full_endpoint" \
  -H "Content-Type: application/json" \
  -H "origin: $origin" \
  -H "X-Gtm-Server-Preview: $gtm_preview_header" \
  -d "$payload"
```

## Send Measurement Protocol requests via Node JS
```js
/*
  NAMELESS ANALYTICS MEASUREMENT PROTOCOL 
  NODE JS EXAMPLE CODE  
  
  Always include in the request:
  - event_name: 
  - event_timestamp:
  - event_origin = 'Measurement Protocol'
  - client_id = 15 chars alphanumeric random string
  - session_id = client_id + 15 chars alphanumeric random string
  - page_id = 15 chars alphanumeric random string
  - event_id = page_id + 15 chars alphanumeric random string
*/

const axios = require('axios');
const crypto = require('crypto');

const full_endpoint = 'https://gtm.tommasomoretti.com/tm/nameless';
const origin = 'https://tommasomoretti.com';
const gtm_preview_header = 'ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NTc1OTkzNmUzOGM2YmQyYzU4Nw==';

const event_date = new Date().toISOString().split('T')[0];
const event_datetime = new Date().toISOString().replace("Z", "000");
const event_timestamp = Date.now();
const processing_event_timestamp = null;
const event_origin = 'Measurement Protocol'
const job_id = crypto.randomBytes(8).toString('hex');
const client_id = '005cKxwvVDPMjG3' // Modify this according to the current user's client_id
const user_id = null // Add it if exists
const user_log = 'Same user, same session'
const session_id = '005cKxwvVDPMjG3_kbNdatKCaN4EWb' // Modify this according to the current user's session_id
const event_name = 'purchase' // Modify this according to the event to be sent
const page_id = 'q4adxB8qx2toy' // Modify this according to the current user's page_id
const event_id = page_id + crypto.randomBytes(13).toString('base64').replace(/[^a-zA-Z0-9]/g, '').slice(0, 13);


// Retrieve this information in real time calling window.get_last_consent_values() JavaScript utility function or later from BigQuery by taking it from the last event recorded on the page of the event to be sent
const respect_consent_mode = "No"; // Not available when using window.get_last_consent_values(). Retrieve this information from the Nameless Analytics Client-side configuration variable tag configuration (optional).
const tracking_anonimization = "No"; // Not available when using window.get_last_consent_values(). Retrieve this information from the Nameless Analytics Client-side configuration variable tag configuration (optional).
const consent_type = "Update";
const ad_user_data = "Granted";
const ad_personalization = "Denied";
const ad_storage = "Granted";
const analytics_storage = "Granted";
const functionality_storage = "Granted";
const personalization_storage = "Granted";
const security_storage = "Granted";

const payload = {
  "event_date": event_date,
  "event_datetime": event_datetime,
  "event_timestamp": event_timestamp,
  "processing_event_timestamp": processing_event_timestamp,
  "event_origin": event_origin,
  "job_id": job_id,
  "client_id": client_id,
  "user_id": user_id,
  "user_log": user_log,
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
};

console.log("----- NAMELESS ANALYTICS -----")
console.log("--------- DATA LOADER --------")
console.log("Function execution start: 🤞")
console.log('👉 Send request to ' + full_endpoint);

const headers = {
  'Content-Type': 'application/json',
  'origin': origin,
  'X-Gtm-Server-Preview': gtm_preview_header,
}

axios.post(full_endpoint, payload, {headers})
  .then((response) => {
    console.log(' ', response.data.response)
    console.log('  👉 Response data:')
    console.log(JSON.stringify(response.data, null, 2).split("\n").map(line => "  " + line).join("\n")); // Uncomment to see full response data from Nameless Analytics Server-side client tag
    console.log("Function execution end: 👍")
  })
  .catch ((error) => {
    try {
      if (error.response && error.response.data) {
        let errorResponse = error.response.data;
        
        console.log(' ', errorResponse.response || 'No data');
      }
      throw error;
    } catch (innerError) {
        console.log('🔴 Request failed:', error.message);
    }
  })
```

## Send Measurement Protocol requests via Python 
```python
# NAMELESS ANALYTICS MEASUREMENT PROTOCOL 
# NODE JS EXAMPLE CODE  
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

full_endpoint = 'https://gtm.tommasomoretti.com/tm/nameless'
origin = 'https://tommasomoretti.com'
gtm_preview_header = 'ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NTc1OTkzNmUzOGM2YmQyYzU4Nw=='

event_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
event_datetime = datetime.now(timezone.utc).isoformat() + '000'
event_timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)
processing_event_timestamp = None
event_origin = 'Measurement Protocol'
job_id = secrets.token_hex(8)
client_id = '005cKxwvVDPMjG3' # Modify this according to the current user's client_id
user_id = None # Add it if exists
user_log = 'Same user, same session'
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
    "user_log": user_log,
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
```
