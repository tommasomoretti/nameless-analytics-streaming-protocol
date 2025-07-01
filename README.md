<picture>
  <source srcset="https://github.com/user-attachments/assets/6af1ff70-3abe-4890-a952-900a18589590" media="(prefers-color-scheme: dark)">
  <img src="https://github.com/user-attachments/assets/9d9a4e42-cd46-452e-9ea8-2c03e0289006">
</picture>

---

# Streaming protocol

The Nameless Analytics Streaming protocol is a python script that sends data to [Nameless Analytics Server-side client tag](https://github.com/tommasomoretti/nameless-analytics-server-side-client-tag/).

For an overview of how Nameless Analytics works [start from here](https://github.com/tommasomoretti/nameless-analytics/).

Table of contents:
- [Required parameters](#required-fields)
- [Send Streaming protocol requests](#send-streaming-protocol-requests)
- [Caveats](#caveats)


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


Please note: Streaming protocol requests do not carry any cookies, and since the Nameless Analytics Server-side client tag relies on cookies in the request to manage new users and new sessions, if a request has event_origin = 'Website' but contains no cookies, new client_id and session_id values will always be created. As a result, the client_id and session_id parameters in the request will be overridden with those values.


---

Reach me at: [Email](mailto:hello@tommasomoretti.com) | [Website](https://tommasomoretti.com/?utm_source=github.com&utm_medium=referral&utm_campaign=nameless_analytics) | [Twitter](https://twitter.com/tommoretti88) | [Linkedin](https://www.linkedin.com/in/tommasomoretti/)
