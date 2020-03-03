DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS recipes;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE recipes (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    job TEXT NOT NULL,
    level INTEGER,
    type TEXT,
    num_crafted INTEGER,
    difficulty INTEGER,
    durability INTEGER,
    max_quality INTEGER
);

-- CREATE TABLE locations (
--     location_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     within INTEGER,
--     name TEXT NOT NULL,
--     type TEXT NOT NULL,
--     FOREIGN KEY (within) REFERENCES locations (location_id)
-- );

-- CREATE TABLE recipes (
--     recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     job TEXT,
--     level INTEGER,
--     type TEXT,
--     num_crafted INTEGER,
--     difficulty INTEGER,
--     durability INTEGER,
--     max_quality INTEGER,
-- );