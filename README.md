<img src="https://github.com/user-attachments/assets/93640f49-d8fb-45cf-925e-6b7075f83927#gh-light-mode-only" alt="Light Mode" />
<img src="https://github.com/user-attachments/assets/71380a65-3419-41f4-ba29-2b74c7e6a66b#gh-dark-mode-only" alt="Dark Mode" />

---

# Streaming protocol

The Nameless Analytics Streaming protocol is a python script that sends data to [Nameless Analytics Server-side client tag](https://github.com/tommasomoretti/nameless-analytics-server-side-client-tag/).

For an overview of how Nameless Analytics works [start from here](https://github.com/tommasomoretti/nameless-analytics/).

Table of contents:
- [Required parameters](#required-fields)
- [Send Streaming protocol requests](#send-streaming-protocol-requests)



## Required parameters

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



## Send requests 
Please note: Always use event_origin 'Streaming protocol'.

---

Reach me at: [Email](mailto:hello@tommasomoretti.com) | [Website](https://tommasomoretti.com/?utm_source=github.com&utm_medium=referral&utm_campaign=nameless_analytics) | [Twitter](https://twitter.com/tommoretti88) | [Linkedin](https://www.linkedin.com/in/tommasomoretti/)
