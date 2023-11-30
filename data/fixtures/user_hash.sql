CREATE TABLE IF NOT EXISTS user_hash (
    user_id VARCHAR(255) PRIMARY KEY,
    password_hash VARCHAR(65535) NOT NULL
);
