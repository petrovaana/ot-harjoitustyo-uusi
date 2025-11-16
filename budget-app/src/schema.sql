DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS logged_spendings;
DROP TABLE IF EXISTS income;
DROP TABLE IF EXISTS monthly_spendings;

CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
);

CREATE TABLE logged_spengings (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    amount INTEGER NOT NULL,
    content TEXT,
    FOREIGN KEY(username) REFERENCES users(username)
);

CREATE TABLE income (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    amount INTEGER NOT NULL,
    content TEXT,
    FOREIGN KEY(username) REFERENCES users(username)
);

CREATE TABLE monthly_spendings (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    amount INTEGER NOT NULL,
    content TEXT,
    FOREIGN KEY(username) REFERENCES users(username)
);