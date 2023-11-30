CREATE TABLE IF NOT EXISTS user_hash_algorithm (
    user_id VARCHAR(255) PRIMARY KEY,
    hash_algorithm VARCHAR(255) NOT NULL
    algorithm_parameters VARCHAR(65535) NOT NULL
);
