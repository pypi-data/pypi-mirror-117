CREATE TABLE IF NOT EXISTS "Container"(
    "Name" TEXT PRIMARY KEY NOT NULL UNIQUE,
    "Hosted" TEXT NOT NULL UNIQUE,
    "Version" VARCHAR(20) NOT NULL,
    "Readme" TEXT DEFAULT "",
    "Common" BOOL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS "Sql"(
    "Hash" INT PRIMARY KEY NOT NULL UNIQUE,
    "SQL" TEXT NOT NULL,
    "EMPTY" BOOLEAN NOT NULL DEFAULT FALSE
);


INSERT OR IGNORE INTO "Container"(
    "Name", "Hosted", "Version", "Common") VALUES (
    "Rash", "https://github.com/RahulARanger/Rash/tree/master/Rash", "0.0.4", TRUE
);


INSERT OR IGNORE INTO "Container"(
"Name", "Hosted", "Version", "Common") VALUES (
"RashLogger", "https://github.com/RahulARanger/Rash/tree/master/RashLogger/RashLogger", "0.0.1", TRUE
);




INSERT OR IGNORE INTO "Sql"(
'Hash', 'SQL') VALUES(
0, "SELECT SQL, Empty FROM Sql WHERE Hash = ?"
);


INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL", "Empty") VALUES (
1, "SELECT Name, Hosted, Version, 'Common' FROM Container;", TRUE
); -- for selecting all entities except markdown in Container


INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES (
2, "SELECT Hosted, Version, Common FROM Container WHERE Name = ?;"
); -- searches in container through Name column


INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES (
3, "SELECT Hosted FROM Container WHERE Name = ?;"
);

INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES (
4, "SELECT Version FROM Container WHERE Name = ?;"
);

INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL", "Empty") VALUES (
5, "SELECT Name FROM Container;", TRUE
);

INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL", "Empty") VALUES (
6, 'SELECT Name FROM  Container WHERE Common == TRUE;', TRUE
);


INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES (
7, "SELECT Readme FROM Container WHERE Name = ?;"
);


INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES(
8, "UPDATE Container SET Version = ? WHERE Name = ?;"
);

INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES(
9, "UPDATE Container SET Readme = ? WHERE Name = ?;"
);

INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES(
10, "INSERT INTO Sql(Name, Hosted, Version, Readme) VALUES(?, ?, ?, ?);"
);

INSERT OR IGNORE INTO "Sql"(
"Hash", "SQL") VALUES(
11, "SELECT Name FROM Container WHERE Hosted = ?"
);
