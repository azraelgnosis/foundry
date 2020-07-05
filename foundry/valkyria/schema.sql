DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS ethnicities;
DROP TABLE IF EXISTS soldiers;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS potentials;
DROP TABLE IF EXISTS map_soldiers_potentials;


CREATE TABLE jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_val TEXT UNIQUE NOT NULL
);

INSERT INTO jobs VALUES (NULL, "Scout");
INSERT INTO jobs VALUES (NULL, "Shocktrooper");
INSERT INTO jobs VALUES (NULL, "Lancer");
INSERT INTO jobs VALUES (NULL, "Enginer");
INSERT INTO jobs VALUES (NULL, "Sniper");

CREATE TABLE ethnicities (
    ethnicity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ethnicity_val TEXT UNIQUE NOT NULL
);

INSERT INTO ethnicities VALUES (NULL, "Gallian");
INSERT INTO ethnicities VALUES (NULL, "Darcsen");

CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    soldier_val TEXT NOT NULL,
    job_id INTEGER NOT NULL,
    sex INTEGER NOT NULL,
    ethnicity_id INTEGER NOT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs (job_id),
    FOREIGN KEY (ethnicity_id) REFERENCES ethnicities (ethnicity_id)
);

CREATE TABLE likes (
    like_id INTEGER PRIMARY KEY AUTOINCREMENT,
    soldier_id INTEGER NOT NULL,
    liked_id INTEGER NOT NULL,
    FOREIGN KEY (soldier_id) REFERENCES soldiers (soldier_id),
    FOREIGN KEY (liked_id) REFERENCES soldiers (soldier_id)
);

CREATE TABLE potentials (
    potential_id INTEGER PRIMARY KEY AUTOINCREMENT,
    potential_val TEXT UNIQUE NOT NULL,
    potential_text TEXT NOT NULL
);

CREATE TABLE map_soldiers_potentials (
    map_id INTEGER PRIMARY KEY AUTOINCREMENT,
    soldier_id INTEGER NOT NULL,
    potential_id INTEGER NOT NULL,
    FOREIGN KEY (soldier_id) REFERENCES soldiers (soldier_id),
    FOREIGN KEY (potential_id) REFERENCES potentials (potential_id)
);