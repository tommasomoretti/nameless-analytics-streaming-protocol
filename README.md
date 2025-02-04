![Na logo beta](https://github.com/tommasomoretti/nameless-analytics/assets/29273232/7d4ded5e-4b79-46a2-b089-03997724fd10)

## Utility functions
Nameless Analytics has a set of utilities that can be called via JavaScript.

### Get client id and session id value 
Send a request to the Server-side GTM Client Tag, which reads the cookies and returns the values of client_id, session_id, and page_id.

<img width="1512" alt="Screenshot 2024-11-03 alle 13 08 16" src="https://github.com/user-attachments/assets/51169268-dbc7-4a64-b09a-74b3b778155f">

Usage:
```javascript
const full_endpoint_domain = 'https://gtm.namelessanalytics.com/tm/nameless'
const payload = {
  "event_name": "get_user_data", 
  "event_origin": "Website"
}
await get_user_data(full_endpoint_domain, payload)
```

### Get the current Consent Mode values
Get the last consent type and values pushed into the dataLayer.

<img width="1512" alt="Screenshot 2024-11-03 alle 13 11 35" src="https://github.com/user-attachments/assets/cfb3314a-3a7d-4938-84e3-9e4c861cc581">

Usage:
```javascript
get_last_consent_values()
```

### Get user agent details
Parse user agent details using [UA Parser js library](https://www.jsdelivr.com/package/npm/ua-parser-js).

<img width="1512" alt="Screenshot 2024-11-03 alle 13 16 02" src="https://github.com/user-attachments/assets/0907137c-c94e-4497-9cd3-484a78f3c396">

Usage:
```javascript
parse_user_agent()
```

### Format timestamp
Format timestamp into datetime string.

<img width="284" alt="Screenshot 2024-11-03 alle 13 20 07" src="https://github.com/user-attachments/assets/f0ccd66b-77f1-47cc-ae6b-7a61a4563eb9">

Usage:
```javascript
const timestamp = Date.now()
format_datetime(timestamp)
```

### Get Channel Grouping 
Giving a source and a campaign name, calculate the standard channel grouping of those values.

<img width="1512" alt="Screenshot 2024-11-03 alle 13 49 09" src="https://github.com/user-attachments/assets/cf6692ac-fd11-44bb-9cbf-22960a9b89e2">

Usage:
```javascript
const source = 'facebook'
const campaign_name = 'test'
get_channel_grouping(source, campaign_name)
```


## Measurament protocol
### Required fields

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

### Send requests via Measurement Protocol
```bash
### Request configurations 
full_endpoint="https://gtm.tommasomoretti.com/tm/nameless"
origin="https://tommasomoretti.com"
gtm_preview_header="ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NGQxMzMyZmZkYWIwY2NmNWFjNg=="

### Request payload required fields
event_date=$(date +%Y-%m-%d)
event_name="purchase"
event_timestamp=$(date -u +%s) 
client_id="8062031855"
session_id="8062031855_2527092995"
page_id="1234328035"
event_id="1234328035_8765438291"

payload=$(cat <<EOF
{
  "event_date": "$event_date",
  "event_name": "$event_name",
  "event_timestamp": "${event_timestamp}000",
  "event_origin": "Measurement Protocol",
  "client_id": "$client_id",
  "session_id": "$session_id",
  "event_data": {
    "page_id": "$page_id",
    "event_id": "$event_id"
  }
}
EOF
)


curl -X POST "$full_endpoint" \
  -H "Content-Type: application/json" \
  -H "origin: $origin" \
  -H "X-Gtm-Server-Preview: $gtm_preview_header" \
  -d "$payload"
```

Response:
```
{
   "status_code":200,
   "response":"🟢 Request claimed succesfully",
   "data":{
      "event_date":"2024-09-08",
      "event_name":"purchase",
      "event_timestamp":"1725796383000",
      "event_origin":"Measurement Protocol",
      "client_id":"8062031855",
      "session_id":"8062031855_2527092995",
      "event_data":{
         "page_id":"8062031855_2527092995-1234328035",
         "event_id":"8062031855_2527092995-1234328035_8765438291",
         "country":"IT",
         "city":"venice",
         "ss_hostname":"gtm.tommasomoretti.com",
         "ss_container_id":"GTM-KQG9ZNG",
         "ss_manual_parameter_firestore":"abcd",
         "ss_manual_parameter":"abcd"
      },
      "received_event_timestamp":1725796383995,
      "content_length":298
   }
}
```

### Get user data via Measurement Protocol
Don't do this. 

Nameless Analytics retrieves client_id, session_id, and page_id values from the browser's request cookies when handling a get_user_data event. Since requests made via the terminal do not contain Nameless Analytics' standard cookies, they are treated as the user's first event of their first visit, generating a new client_id, session_id, and page_id with each request.

For this reason the response will be 500 - 🔴 You can not retreive user_data from measurement protocol

```bash
# Request configurations 
full_endpoint="https://gtm.tommasomoretti.com/tm/nameless"
origin="https://tommasomoretti.com"
gtm_preview_header="ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5M2QwMzEwMWIwM2JhNzBiNjY4Mg=="

# Request payload required fields
event_name="get_user_data"

payload=$(cat <<EOF
{
  "event_name": "$event_name",
  "event_origin": "Measurement Protocol"
}
EOF
)


curl -X POST "$full_endpoint" \
  -H "Content-Type: application/json" \
  -H "origin: $origin" \
  -H "X-Gtm-Server-Preview: $gtm_preview_header" \
  -d "$payload"
```
Response:
```
{
   "status_code":500,
   "response":"🔴 You can not retreive user_data from measurement protocol"
}
```
