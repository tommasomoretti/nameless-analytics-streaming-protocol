![Na logo beta](https://github.com/tommasomoretti/nameless-analytics/assets/29273232/7d4ded5e-4b79-46a2-b089-03997724fd10)

## Utility functions
### Get client id and session id value 
(E.g.: full_endpoint_domain = 'https://gtm.namelessanalytics.com/tm/nameless')
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
(E.g.: timestamp = 1724336713016 => '2024-08-22T14:25:13.016000') 
```javascript
format_datetime(timestamp)
```

### Get Channel Grouping 
(E.g.: source = 'facebook', campaign = 'test')
```javascript
get_channel_grouping(source, campaign)
```


## Measurement Protocol
Lorem ipsum

```bash
set full_endpoint="https://gtm.tommasomoretti.com/tm/nameless"
set origin="https://tommasomoretti.com"
set gtm_preview_header="ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5MThmMjVhMTQwNWViZjcwYmE5Yw==" 
set payload='{
       "event_name": "pv",
       "event_timestamp": 123456789,
       "client_id": "4079777164",
       "session_id": "4079777164_8768230534",
       "from_measurement_protocol": "Yes",
       "event_data": {
         "page_id": "1105347900",
         "event_id": "1105347900_2273450297"
       }
     }'

curl -X POST $full_endpoint \
  -H "Content-Type: application/json" \
  -H "origin: $origin" \
  -H "X-Gtm-Server-Preview: $gtm_preview_header" \
  -d $payload
```
