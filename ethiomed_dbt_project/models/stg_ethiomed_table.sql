-- models/stg_ethiomed_table.sql
WITH raw_data AS (
    SELECT
        channel,
        messageid,
        date,
        senderid,
        messagecontent,
        views,
        comments,
        reactions
    FROM {{ source('public', 'ethiomed_table') }}
)
SELECT * FROM raw_data
