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
const gtm_preview_header = 'ZW52LTEwMnxUWk9Pd1l1SW5YWFU0eFpzQlMtZHN3fDE5NTgwZDIzMDZmNGY0ZDEwZmM2Mg==';

const timestamp = Date.now()
const formatted_datetime = format_datetime(timestamp);

const event_date = formatted_datetime.date;
const event_datetime = formatted_datetime.date_time_micros;
const event_timestamp = timestamp
const processing_event_timestamp = null;
const event_origin = 'Measurement Protocol'
const job_id = crypto.randomBytes(8).toString('hex');
const client_id = '005cKxwvVDPMjG3' // Modify this according to the current user's client_id
const user_id = null // Add it if exists
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


// Format timestamp into date 
function format_datetime(timestamp) {
  const date = new Date(timestamp)

  const year = date.getUTCFullYear()
  const month = String(date.getUTCMonth() + 1).padStart(2, '0')
  const day = String(date.getUTCDate()).padStart(2, '0')
  const hours = String(date.getUTCHours()).padStart(2, '0')
  const minutes = String(date.getUTCMinutes()).padStart(2, '0')
  const seconds = String(date.getUTCSeconds()).padStart(2, '0')
  const milliseconds = String(date.getUTCMilliseconds()).padStart(3, '0')

  const formatted_date = {
    date: `${year}-${month}-${day}`,
    date_time: `${year}-${month}-${day}T${hours}:${minutes}:${seconds}`,
    date_time_millis: `${year}-${month}-${day}T${hours}:${minutes}:${seconds}` + `.${milliseconds}`,
    date_time_micros: `${year}-${month}-${day}T${hours}:${minutes}:${seconds}` + `.${milliseconds}000`,
    year: year,
    month: month,
    day: day,
    hours: hours,
    minutes: minutes,
    seconds: seconds,
    milliseconds: `.${milliseconds}`,
    microseconds: `.${milliseconds}000`
  }

  return formatted_date
}