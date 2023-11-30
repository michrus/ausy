CREATE TABLE IF NOT EXISTS user_data (
    user_id VARCHAR PRIMARY KEY,
    username VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    access_level VARCHAR NOT NULL
);
