DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS spells;
DROP TABLE IF EXISTS schools;

CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    val TEXT NOT NULL
);

CREATE TABLE schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    val TEXT NOT NULL
);

CREATE TABLE spells (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    val TEXT NOT NULL,
    level INTEGER,
    school_id INTEGER,
    cast_time INTEGER,
    ritual INTEGER DEFAULT 0,
    range INTEGER,
    duration INTEGER,
    components TEXT,
    description TEXT,
    FOREIGN KEY (school_id) REFERENCES schools (id)
);

CREATE TABLE map_spells_classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    spell_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    FOREIGN KEY (spell_id) REFERENCES spells (id),
    FOREIGN KEY (class_id) REFERENCES class (id)
);