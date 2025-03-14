# NAMELESS ANALYTICS MEASUREMENT PROTOCOL 
# BASH EXAMPLE CODE  
# 
# Always include in the request:
# - event_name: 
# - event_timestamp:
# - event_origin = 'Measurement Protocol'
# - client_id = 15 chars alphanumeric random string
# - session_id = client_id + 15 chars alphanumeric random string
# - page_id = 15 chars alphanumeric random string
# - event_id = page_id + 15 chars alphanumeric random string

full_endpoint="https://gtm.tommasomoretti.com/tm/nameless"
origin="https://tommasomoretti.com"
gtm_preview_header="ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NTgwZDIzMDZmNGY0ZDEwZmM2Mg=="

event_date=$(date +%Y-%m-%d)
event_datetime=$(date -u +"%Y-%m-%dT%H:%M:%S.%3N00" | sed 's/N/00/')
event_timestamp="$(($(date -u +%s) * 1000))"
processing_event_timestamp=null
event_origin="Measurement Protocol"
job_id="$(openssl rand -hex 6)"
client_id="005cKxwvVDPMjG3" # Modify this according to the current user's client_id
user_id=null # Add it if exists
session_id="005cKxwvVDPMjG3_kbNdatKCaN4EWb" # Modify this according to the current user's session_id
event_name="purchase" # Modify this according to the event to be sent
page_id="q4adxB8qx2toy" # Modify this according to the current user's page_id
event_id="${page_id}_$(openssl rand -hex 6)"

# Retrieve this information in real time calling window.get_last_consent_values() JavaScript utility function or later from BigQuery by taking it from the last event recorded on the page of the event to be sent
respect_consent_mode="No" # Not available when using window.get_last_consent_values(). Retrieve this information from the Nameless Analytics Client-side configuration variable tag configuration (optional).
tracking_anonimization="No" # Not available when using window.get_last_consent_values(). Retrieve this information from the Nameless Analytics Client-side configuration variable tag configuration (optional).
consent_type="Update"
ad_user_data="Granted"
ad_personalization="Denied"
ad_storage="Granted"
analytics_storage="Granted"
functionality_storage="Granted"
personalization_storage="Granted"
security_storage="Granted"

payload=$(cat <<EOF
{
    "event_date": "$event_date",
    "event_datetime": "$event_datetime",
    "event_timestamp": "$event_timestamp",
    "processing_event_timestamp": "$processing_event_timestamp",
    "event_origin": "$event_origin",
    "job_id": "$job_id",
    "client_id": "$client_id",
    "user_id": "$user_id",
    "session_id": "$session_id",
    "event_name": "$event_name",
    "event_data": {
        "page_id": "$page_id",
        "event_id": "$event_id"
    }, 
    "consent_data": {
        "respect_consent_mode": "$respect_consent_mode",
        "tracking_anonimization": "$tracking_anonimization",
        "consent_type": "$consent_type",
        "ad_user_data": "$ad_user_data",
        "ad_personalization": "$ad_personalization",
        "ad_storage": "$ad_storage",
        "analytics_storage": "$analytics_storage",
        "functionality_storage": "$functionality_storage",
        "personalization_storage": "$personalization_storage",
        "security_storage": "$security_storage"
    }
}
EOF
)

curl -X POST "$full_endpoint" \
    -H "Content-Type: application/json" \
    -H "origin: $origin" \
    -H "X-Gtm-Server-Preview: $gtm_preview_header" \
    -d "$payload"
