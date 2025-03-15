![Na logo beta](https://github.com/tommasomoretti/nameless-analytics/assets/29273232/7d4ded5e-4b79-46a2-b089-03997724fd10)

---

# Measurament protocol

The Nameless Analytics Measurement Protocol is a method for send data to [Nameless Analytics Server-side client tag](https://github.com/tommasomoretti/nameless-analytics-server-side-client-tag).

For an overview of how Nameless Analytics works [start from here](https://github.com/tommasomoretti/nameless-analytics).

Start from here:
- [Required fields](#required-fields)
- [Send Measurement Protocol requests](#send-measurement-protocol-requests)



## Required fields

| Field name                | Example value | Description                 |
|-----------------|---------------|---------------------------------------|
| event_origin    | Yes           | Measurament Protocol                  |
| event_date      | 2024-01-01    | Event date                            |
| event_name      | purchase      | Event name (do not use get_user_data) |
| event_timestamp | 1722607958646 | Event timestamp in milliseconds       |
| client_id       |               |                                       |
| session_id      |               |                                       |
| page_id         |               |                                       |
| event_id        |               |                                       |



## Send Measurement Protocol requests 
```python
```
