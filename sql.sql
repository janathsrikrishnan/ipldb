-- CREATE TABLE iplEdition(editionNo int PRIMARY KEY, name varchar(30), sponsor varchar(20),
-- 						years int, champion varchar(30), host varchar(30));
-- CREATE TABLE team(team_id int PRIMARY KEY, team_name varchar(30), coach varchar(30),
-- 				  owner varchar(30), captain varchar(30), editionNo int);

-- CREATE TABLE point_table(editionNo int, team_id int, won int, last int, draw int, netRunRate numeric(6, 3),
-- 						points int, PRIMARY KEY(editionNo, team_id));


-- CREATE TABLE players(playerId int, playerName varchar(30), role varchar(10), runs int, wickets int,
-- 					nationality varchar(30));
-- CREATE TABLE seasonStatus(editionNo int PRIMARY KEY, winner int, runner int, orangeCap int, purpleCap int);

-- CREATE TABLE matchStatus(editionNo int, matchNO int, team1 int, team2 int, winner int,
-- 						 score1 int, wicket1 int, over1 numeric(3, 1), score2 int, wicket2 int, over2 numeric(3,1));