CREATE TABLE IF NOT EXISTS user_salt (
    user_id VARCHAR PRIMARY KEY,
    password_salt VARCHAR NOT NULL
);
