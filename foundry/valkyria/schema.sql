DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS soldiers;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS potentials;
DROP TABLE IF EXISTS map_soldiers_potentials;


CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    val TEXT NOT NULL,
);

CREATE TABLE soldiers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    val TEXT NOT NULL,
    job_id INTEGER NOT NULL
);

CREATE TABLE likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    soldier_id INTEGER NOT NULL,
    liked_id INTEGER NOT NULL,
    FOREIGN KEY (soldier_id) REFERENCES soldiers (id),
    FOREIGN KEY (liked_id) REFERENCES soldiers (id)
);

CREATE TABLE potentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    val TEXT NOT NULL
);

CREATE TABLE map_soldiers_potentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    soldier_id INTEGER NOT NULL,
    potential_id INTEGER NOT NULL,
    FOREIGN KEY (soldier_id) REFERENCES soldiers (id),
    FOREIGN KEY (potential_id) REFERENCES potentials (id)
);