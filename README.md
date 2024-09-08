![Na logo beta](https://github.com/tommasomoretti/nameless-analytics/assets/29273232/7d4ded5e-4b79-46a2-b089-03997724fd10)

## Utility functions
### Get client id and session id value 
```javascript
const full_endpoint_domain = 'https://gtm.namelessanalytics.com/tm/nameless'
const payload = {
  "event_name": "get_user_data", 
  "from_measurement_protocol": "No"
}
await get_user_data(full_endpoint_domain, payload)
```

### Get the current Consent Mode values
```javascript
get_last_consent_values()
```

### Get user agent details
```javascript
parse_user_agent()
```

### Format timestamp into date 
```javascript
const timestamp = 1724336713016
format_datetime(timestamp)
```

### Get Channel Grouping 
```javascript
const source = 'facebook'
const campaign = 'test'
get_channel_grouping(source, campaign)
```


## Measurament protocol
### Required fields

| Field name      | Example value | Description                     |
|-----------------|---------------|---------------------------------|
| event_date      | 2024-01-01    | Event date                      |   
| event_name      | purchase      | Event name                      |
| event_timestamp | 1722607958646 | Event timestamp in milliseconds |
| client_id       | | |
| session_id      | | |
| page_id         | | |
| event_id        | | |

### Send requests via Measurement Protocol
```bash
### Request configurations 
full_endpoint="https://gtm.tommasomoretti.com/tm/nameless"
origin="https://tommasomoretti.com"
gtm_preview_header="ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5MWEzYzMxNzJiYTI3OWM2MDYxMg=="

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
  "from_measurement_protocol": "Yes",
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


### Get user data via Measurement Protocol (DONT DO THIS!)
```bash
# Request configurations 
full_endpoint="https://gtm.tommasomoretti.com/tm/nameless"
origin="https://tommasomoretti.com"
gtm_preview_header="ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5MWEzYzMxNzJiYTI3OWM2MDYxMg=="

# Request payload required fields
event_name="get_user_data"

payload=$(cat <<EOF
{
  "event_name": "$event_name",
  "from_measurement_protocol": "Yes"
}
EOF
)


curl -X POST "$full_endpoint" \
  -H "Content-Type: application/json" \
  -H "origin: $origin" \
  -H "X-Gtm-Server-Preview: $gtm_preview_header" \
  -d "$payload"
```
