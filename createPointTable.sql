CREATE TABLE pointTable(editionNo int, TeamName varchar(30),
						played int, won int, lost int, Tied int, NR int,
						NetRunRate numeric(6,3),For_ varchar(30), Against varchar(30),
						points int);
-- DROP TABLE pointTable;
COPY pointTable FROM 'D:\ipldb\pointsTableEdited.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM pointTable;
ALTER TABLE pointTable ADD CONSTRAINT pk PRIMARY KEY(editionNo, TeamName);
