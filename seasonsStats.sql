CREATE TABLE seasonStats (editionNo int , Team varchar(30), 
						 TeamName varchar(40), coach varchar(30),
						 owner varchar(60), captian varchar(30));

DROP TABLE seasonStats;
COPY seasonStats FROM 'D:\ipldb\teams_fullnames - teams_fullnames.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM seasonStats;
UPDATE seasonStats SET teamname='Deccan Chargers' WHERE team='DEC'; 