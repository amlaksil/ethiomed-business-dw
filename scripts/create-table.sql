-- Connect to the database
\c ethiomed_db

-- Drop the table if it exists
DROP TABLE IF EXISTS ethiomed_table;

-- Create the table named ethiomed_table
CREATE TABLE ethiomed_table (
    Channel TEXT,
    messageId BIGINT,
    Date TIMESTAMP,
    SenderId BIGINT,
    MessageContent TEXT,
    Views DOUBLE PRECISION,
    Comments DOUBLE PRECISION,
    Reactions DOUBLE PRECISION
);

-- Load data from a CSV file using the \copy command
\copy ethiomed_table(Channel, messageId, Date, SenderId, MessageContent, Views, Comments, Reactions) FROM 'data/cleaned_data.csv' CSV HEADER;
