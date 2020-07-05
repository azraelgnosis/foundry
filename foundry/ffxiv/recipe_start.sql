-- SQLite
INSERT INTO `components` (name)
VALUES ("Bladder Component Materials");

-- SQLite
INSERT INTO `recipes` (name, level, type, yield, difficulty, durability, max_quality, crystalA, num_crystalA, crystalB, num_crystalB)
VALUES ("Bladder Component", 1, "Other", 1, 19, 60, 312, "Wind Shard", 1, "Ice Shard", 1);

-- SQLite
INSERT INTO `map_recipe_component` (recipe_fk, component_fk, num)
VALUES (1, 1, 1);