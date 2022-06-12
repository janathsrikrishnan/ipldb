-- CREATE TABLE purpleCap (editionNo int, position int, playerId int, 
-- 						playerName char(40), wickets int, BestBowledInnings varchar(30),
-- 						teamName varchar(40));
-- DROP TABLE purpleCap;
-- COPY purpleCap FROM 'D:\ipldb\Purple Cap.csv' DELIMITER ',' CSV HEADER;
-- SELECT * FROM purpleCap;

-- CREATE TABLE orangecap (editionNo int, position int, playerId int, playername varchar(40), runs int,
-- 					   highestScore varchar(10), teamname varchar(40));
-- DROP TABLE orangecap;
COPY orangecap FROM 'D:\ipldb\Orange Cap (2).csv' DELIMITER ',' CSV HEADER;					 

-- CREATE TABLE matchs (editionNo int, firstbatting varchar(100),
-- 					secondbatting varchar(100), matchname varchar(200),
-- 					matchdate varchar(12), commentss varchar(200), 
-- 					firstsummary varchar(60), secondsummary varchar(60));
-- COPY matchs FROM 'D:\ipldb\match.csv' DELIMITER ',' CSV HEADER;