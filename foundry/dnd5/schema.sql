DROP TABLE IF EXISTS spells;

CREATE TABLE spells (
    spell_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level INTEGER,
    school TEXT,
    cast_time INTEGER,
    range INTEGER,
    duration INTEGER,
    components TEXT,
    description TEXT
);