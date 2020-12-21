DROP schema Dota;
CREATE DATABASE Dota;
USE Dota ;

CREATE TABLE dota_user( 
user_id BIGINT PRIMARY KEY NOT NULL, 
user_name VARCHAR(45) NOT NULL, 
user_email VARCHAR(45) NOT NULL,
user_username VARCHAR (30) NOT NULL unique,
user_password VARCHAR(30) NOT NULL);

CREATE TABLE dota_admin( 
admin_id BIGINT PRIMARY KEY NOT NULL,  
admin_registration_number VARCHAR(20) NOT NULL UNIQUE, 
FOREIGN KEY (admin_id) REFERENCES dota_user(user_id) ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE dota_gamer( 
gamer_id BIGINT PRIMARY KEY NOT NULL, 
gamer_ign VARCHAR(20) NOT NULL, 
FOREIGN KEY (gamer_id) REFERENCES dota_user(user_id) ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE dota_premiumuser( 
premiumuser_Gamer_ID BIGINT NOT NULL,
premiumuser_Registration_Number BIGINT PRIMARY KEY NOT NULL, 
premiumuser_RegistrationExpiryDate VARCHAR(30) NOT NULL,
FOREIGN KEY (premiumuser_Gamer_ID) REFERENCES dota_gamer(gamer_id) ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE dota_mmr( 
mmr_Id BIGINT PRIMARY KEY NOT NULL, 
mmr_score BIGINT NOT NULL DEFAULT 0, 
mmr_medal VARCHAR(30) NOT NULL DEFAULT 'Herald', 
FOREIGN KEY (mmr_id) REFERENCES dota_gamer(gamer_id) ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE TABLE dota_match( 
match_ID INT PRIMARY KEY NOT NULL, 
match_Status VARCHAR(15) NOT NULL, 
match_GPM INT NOT NULL , 
match_Kills INT NOT NULL,
match_XPM INT NOT NULL,
match_death INT NOT NULL,
match_assist INT NOT NULL
);

CREATE TABLE dota_tournament( 
Tournament_ID INT PRIMARY KEY, 
Tournament_name VARCHAR(100) NOT NULL, 
Tournament_starting_timedate DATETIME NOT NULL, 
Tournament_prize INT);

CREATE TABLE dota_gamer_match_tournament( 
matchid INT PRIMARY KEY NOT NULL, 
gamerid BIGINT NOT NULL, 
tournamentid INT,
FOREIGN KEY (matchid) REFERENCES dota_match(match_ID) ON UPDATE CASCADE ON DELETE NO ACTION,
FOREIGN KEY (gamerid) REFERENCES dota_gamer(gamer_ID) ON UPDATE CASCADE ON DELETE NO ACTION,
FOREIGN KEY (tournamentid) REFERENCES dota_tournament(tournament_ID) ON UPDATE CASCADE ON DELETE NO ACTION
);
