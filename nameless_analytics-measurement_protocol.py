# NAMELESS ANALYTICS

declare project_name string default 'tom-moretti';  -- Change this
declare dataset_name string default 'nameless_analytics'; -- Change this
declare dataset_location string default 'eu'; -- Change this

# Tables
declare main_table_name string default 'events_raw';
declare dates_table_name string default 'calendar_dates';

declare main_dataset_path string default CONCAT('`', project_name, '.', dataset_name, '`');
declare main_table_path string default CONCAT('`', project_name, '.', dataset_name, '.', main_table_name,'`');
declare dates_table_path string default CONCAT('`', project_name, '.', dataset_name, '.', dates_table_name,'`');

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Enable BigQuery advanced runtime (for more info https://cloud.google.com/bigquery/docs/advanced-runtime)
declare enable_bigquery_advanced_runtime string default format(
  """
    ALTER PROJECT `%s`
    SET OPTIONS (
      `region-%s.query_runtime` = 'advanced' # default null
    );
  """
, project_name, dataset_location);



# Main dataset (for more info https://cloud.google.com/bigquery/docs/datasets#sql)
declare main_dataset_sql string default format(
  """
    create schema if not exists %s
    options (
      # default_kms_key_name = 'KMS_KEY_NAME',
      # default_partition_expiration_days = PARTITION_EXPIRATION,
      # default_table_expiration_days = TABLE_EXPIRATION,
      # max_time_travel_hours = HOURS, # default 168 hours => 7 days 
      # storage_billing_model = BILLING_MODEL # Phytical or logical (default)  
      description = 'Nameless Analytics',
      location = '%s'
    );
  """
, main_dataset_path, dataset_location);


# Main table
declare main_table_sql string default format(
  """
    create table if not exists %s (
      event_date DATE NOT NULL OPTIONS (description = 'Date of the request'),
      event_datetime DATETIME OPTIONS (description = 'Datetime of the request'),
      event_timestamp INT64 NOT NULL OPTIONS (description = 'Insert timestamp of the event'),
      processing_event_timestamp INT64 OPTIONS (description = ' Nameless Analytics Server-side Client Tag received event timestamp when hits are sent from a website or a Streaming Protocol request. Script start execution timestamp if hits are imported by Nameless Analytics Data Loader.'),
      event_origin STRING NOT NULL OPTIONS (description = '"Streaming Protocol" if the hit comes from streaming protocol, "Website" if the hit comes from browser'),
      content_length INT64 OPTIONS (description = 'Size of the message body, in bytes'),
      client_id STRING NOT NULL OPTIONS (description = 'Client ID'),
      user_data ARRAY<
        STRUCT<
          name STRING OPTIONS (description = 'User data parameter name'),
          value STRUCT<
            string STRING OPTIONS (description = 'User data parameter string value'),
            int INT64 OPTIONS (description = 'User data parameter int number value'),
            float FLOAT64 OPTIONS (description = 'User data parameter float number value'),
            json JSON OPTIONS (description = 'User data parameter JSON value')
          > OPTIONS (description = 'User data parameter value name')
        >
      > OPTIONS (description = 'User data'),
      session_id STRING NOT NULL OPTIONS (description = 'Session ID'),
      session_data ARRAY<
        STRUCT<
          name STRING OPTIONS (description = 'Session data parameter name'),
          value STRUCT<
            string STRING OPTIONS (description = 'Session data parameter string value'),
            int INT64 OPTIONS (description = 'Session data parameter int number value'),
            float FLOAT64 OPTIONS (description = 'Session data parameter float number value'),
            json JSON OPTIONS (description = 'Session data parameter JSON value')
          > OPTIONS (description = 'Session data parameter value name')
        >
      > OPTIONS (description = 'Session data'),   
      event_id STRING NOT NULL OPTIONS (description = 'Event ID'),
      event_name STRING NOT NULL OPTIONS (description = 'Event name'),
      event_data ARRAY<
        STRUCT<
          name STRING OPTIONS (description = 'Event data parameter name'),
          value STRUCT<
            string STRING OPTIONS (description = 'Event data parameter string value'),
            int INT64 OPTIONS (description = 'Event data parameter int number value'),
            float FLOAT64 OPTIONS (description = 'Event data parameter float number value'),
            json JSON OPTIONS (description = 'Event data parameter JSON value')
          > OPTIONS (description = 'Event data parameter value name')
        >
      > OPTIONS (description = 'Event data'),
      ecommerce JSON OPTIONS (description = 'Ecommerce object'),
      datalayer JSON OPTIONS (description = 'Current dataLayer value'),
      consent_data ARRAY<
        STRUCT<
          name STRING OPTIONS (description = 'Consent data parameter name'),
          value STRUCT<
            string STRING OPTIONS (description = 'Consent data parameter string value')
          > OPTIONS (description = 'Consent data parameter value name')
        >
      > OPTIONS (description = 'Consent data')
    )
    PARTITION BY event_date
    CLUSTER BY client_id, session_id, event_name
    OPTIONS (description = 'Nameless Analytics | Main table');
  """
, main_table_path);

<<<<<<< Updated upstream

# Dates table
declare dates_table_sql string default FORMAT(
  """
    create table if not exists %s (
      date DATE NOT NULL OPTIONS(description = "The date value"),
      year INT64 OPTIONS(description = "Year extracted from the date"),
      quarter INT64 OPTIONS(description = "Quarter of the year (1-4) extracted from the date"),
      month_number INT64 OPTIONS(description = "Month number of the year (1-12) extracted from the date"),
      month_name STRING OPTIONS(description = "Full name of the month (e.g., January) extracted from the date"),
      week_number_sunday INT64 OPTIONS(description = "Week number of the year, starting on Sunday"),
      week_number_monday INT64 OPTIONS(description = "Week number of the year, starting on Monday"),  
      day_number INT64 OPTIONS(description = "Day number of the month (1-31)"),
      day_name STRING OPTIONS(description = "Full name of the day of the week (e.g., Monday)"),
      day_of_week_number INT64 OPTIONS(description = "Day of the week number (1 for Monday, 7 for Sunday)"),
      is_weekend BOOL OPTIONS(description = "True if the day is Saturday or Sunday")
    ) PARTITION BY DATE_TRUNC(date, year)
      CLUSTER BY month_name, day_name
      OPTIONS (description = 'Nameless Analytics | Dates utility table')
      AS
    (
      SELECT 
        date,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(QUARTER FROM date) AS quarter,
        EXTRACT(MONTH FROM date) AS month_number,
        FORMAT_DATE('%%B', date) AS month_name,
        EXTRACT(WEEK(SUNDAY) FROM date) AS week_number_sunday,
        EXTRACT(WEEK(MONDAY) FROM date) AS week_number_monday,
        EXTRACT(DAY FROM date) AS day_number,
        FORMAT_DATE('%%A', date) AS day_name,
        EXTRACT(DAYOFWEEK FROM date) AS day_of_week_number, 
        IF(EXTRACT(DAYOFWEEK FROM date) IN (1, 7), TRUE, FALSE) AS is_weekend
      FROM UNNEST(GENERATE_DATE_ARRAY('1970-01-01', '2050-12-31', INTERVAL 1 DAY)) AS date
    );
  """
, dates_table_path);
=======
event_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
event_datetime = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec='microseconds')
event_timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)
processing_event_timestamp = None
event_origin = 'Streaming protocol'
client_id = 'iURYgLE478F7TZU' # Modify this according to the current user's client_id
user_id = None # Add it if exists
session_id = 'iURYgLE478F7TZU_vh5IxJjEiYxKOhh' # Modify this according to the current user's session_id
event_name = 'purchase' # Modify this according to the event to be sent
page_id = 'A4adxB8qx2tZy' # Modify this according to the current user's page_id
event_id = f'{page_id}_{secrets.token_hex(8)}'
>>>>>>> Stashed changes


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Create tables 
execute immediate enable_bigquery_advanced_runtime;
execute immediate main_dataset_sql;
execute immediate main_table_sql;
execute immediate dates_table_sql;
