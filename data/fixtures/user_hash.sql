CREATE TABLE IF NOT EXISTS user_hash (
    user_id VARCHAR PRIMARY KEY,
    password_hash VARCHAR NOT NULL
);
