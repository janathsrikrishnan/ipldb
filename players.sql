-- CREATE TABLE players(editionNo int, TeamName varchar(40), playerId int, PlayerName varchar(100),
-- 					role varchar(100), BattingStyle varchar(40), BowlingStyle varchar(40), Nationality varchar(40), 
-- 					dob char(20), Debut int, Matches int, runs varchar(10), wickets int, photo varchar(200));

-- DROP TABLE players;
COPY players FROM 'D:\ipldb\players.csv' DELIMITER ',' CSV HEADER;