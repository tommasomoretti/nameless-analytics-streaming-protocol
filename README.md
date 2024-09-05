![Na logo beta](https://github.com/tommasomoretti/nameless-analytics/assets/29273232/7d4ded5e-4b79-46a2-b089-03997724fd10)


## Measurement Protocol
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
