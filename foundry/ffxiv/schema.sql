DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS materials;

CREATE TABLE recipes (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    job TEXT NOT NULL,
    level INTEGER,
    type TEXT,
    num_crafted INTEGER,
    difficulty INTEGER,
    durability INTEGER,
    max_quality INTEGER,
)