DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS recipe_materials;
DROP TABLE IF EXISTS components;
DROP TABLE IF EXISTS map_recipe_component;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS recipes;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE recipes (
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level INTEGER,
    type TEXT,
    yield INTEGER,
    difficulty INTEGER,
    durability INTEGER,
    max_quality INTEGER,
    crystalA TEXT,
    num_crystalA INTEGER,
    crystalB Text,
    num_crystalB INTEGER
);

CREATE TABLE components (
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE map_recipe_component (
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_fk INTEGER NOT NULL,
    component_fk INTEGER NOT NULL,
    num INTEGER NOT NULL,
    FOREIGN KEY (recipe_fk) REFERENCES recipes (pk),
    FOREIGN KEY (component_fk) REFERENCES components (pk)
);