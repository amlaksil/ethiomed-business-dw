-- models/transform_ethiomed_table.sql
WITH clean_data AS (
    SELECT
        channel,
        messageid,
        date,
        senderid,
        messagecontent,
        COALESCE(views, 0) AS Views,
        COALESCE(comments, 0) AS Comments,
        COALESCE(reactions, 0) AS Reactions
    FROM {{ ref('stg_ethiomed_table') }}
)
SELECT
    Channel,
    COUNT(DISTINCT messageId) AS message_count,
    SUM(views) AS total_views,
    SUM(comments) AS total_comments,
    SUM(reactions) AS total_reactions
FROM clean_data
GROUP BY channel
