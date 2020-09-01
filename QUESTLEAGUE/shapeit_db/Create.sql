CREATE DATABASE shapeit;
USE shapeit;
CREATE TABLE addproduct (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    gamename VARCHAR(80) NOT NULL, 
    Game_Mode VARCHAR(80) NOT NULL,
    Tournament_Type VARCHAR(80) NOT NULL,
    Tournament_Title VARCHAR(80) NOT NULL,

	Prize_Pot NUMERIC(10, 2) NOT NULL, 
	Entery_Cost NUMERIC(10, 2) NOT NULL,
   	Maximum_Participants NUMERIC(10) NOT NULL,
   	Minimum_Participants NUMERIC(10) NOT NULL,
    Enroled_Participants NUMERIC(10) NOT NULL,

    Platform VARCHAR(80) NOT NULL,
    Starting_Date VARCHAR(80) NOT NULL,
    Tournament_Time VARCHAR(80) NOT NULL,
    Game_Settings VARCHAR(80) NOT NULL,
    Rule_Group VARCHAR(80) NOT NULL,
    Number_Of_Rounds VARCHAR(80) NOT NULL,
    Region VARCHAR(80) NOT NULL,
    Potential_Profit VARCHAR(80) NOT NULL,
    Actual_Profit VARCHAR(80) NOT NULL,
 
	name VARCHAR(80) NOT NULL, 
	price NUMERIC(10, 2) NOT NULL, 
	discount INTEGER, 
	stock INTEGER NOT NULL, 
	colors TEXT NOT NULL, 
	size TEXT NOT NULL, 
	descrip TEXT NOT NULL, 
	pub_date DATETIME NOT NULL, 
	category_id INTEGER NOT NULL, 
	brand_id INTEGER NOT NULL, 
	image_1 VARCHAR(150) NOT NULL, 
	image_2 VARCHAR(150) NOT NULL, 
	image_3 VARCHAR(150) NOT NULL
	-- PRIMARY KEY (id)
	-- FOREIGN KEY(category_id) REFERENCES category (id), 
	-- FOREIGN KEY(brand_id) REFERENCES brand (id)
);

CREATE TABLE category (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(30) NOT NULL, 
	UNIQUE (name)
);

CREATE TABLE register (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(50), 
	username VARCHAR(50), 
	email VARCHAR(50), 
	password VARCHAR(200), 
	country VARCHAR(50), 
	city VARCHAR(50), 
	contact VARCHAR(50), 
	address VARCHAR(50), 
	zipcode VARCHAR(50), 
	profile VARCHAR(200), 
	date_created DATETIME NOT NULL, 
	UNIQUE (username), 
	UNIQUE (email)
);


CREATE TABLE addproductz (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Game_Name VARCHAR(80) NOT NULL, 
    Game_Mode VARCHAR(80) NOT NULL,
    Tournament_Type VARCHAR(80) NOT NULL,
    Tournament_Title VARCHAR(80) NOT NULL,

	Prize_Pot NUMERIC(10, 2) NOT NULL, 
	Entery_Cost NUMERIC(10, 2) NOT NULL,
   	Maximum_Participants NUMERIC(10, 2) NOT NULL,
   	Minimum_Participants NUMERIC(10, 2) NOT NULL,
    Enroled_Participants NUMERIC(10, 2) NOT NULL,

    Platform VARCHAR(80) NOT NULL,
    Starting_Date VARCHAR(80) NOT NULL,
    Tournament_Time VARCHAR(80) NOT NULL,
    Game_Settings VARCHAR(80) NOT NULL,
    Rule_Group VARCHAR(80) NOT NULL,
    Number_Of_Rounds VARCHAR(80) NOT NULL,
    Region VARCHAR(80) NOT NULL,
    Potential_Profit VARCHAR(80) NOT NULL,
    Actual_Profit VARCHAR(80) NOT NULL,




	name VARCHAR(80) NOT NULL, 
	price NUMERIC(10, 2) NOT NULL, 
	discount INTEGER, 
	stock INTEGER NOT NULL, 
	colors TEXT NOT NULL, 
	descrip TEXT NOT NULL, 
	pub_date DATETIME NOT NULL, 
	category_id INTEGER NOT NULL, 
	brand_id INTEGER NOT NULL, 
	image_1 VARCHAR(150) NOT NULL, 
	image_2 VARCHAR(150) NOT NULL, 
	image_3 VARCHAR(150) NOT NULL
	-- PRIMARY KEY (id)
	-- FOREIGN KEY(category_id) REFERENCES category (id), 
	-- FOREIGN KEY(brand_id) REFERENCES brand (id)
);
-- 18

CREATE TABLE customer_order (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	invoice VARCHAR(20) NOT NULL, 
	status VARCHAR(20) NOT NULL, 
	customer_id INTEGER NOT NULL, 
	date_created DATETIME NOT NULL, 
	orders TEXT, 
	UNIQUE (invoice)
);

CREATE TABLE register2 (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(50), 
	username VARCHAR(50), 
	email VARCHAR(50), 
	password VARCHAR(200), 
	country VARCHAR(50), 
	city VARCHAR(50), 
	contact VARCHAR(50), 
	address VARCHAR(50), 
	zipcode VARCHAR(50), 
	profile VARCHAR(200), 
	date_created DATETIME NOT NULL, 
	UNIQUE (username), 
	UNIQUE (email)
);

CREATE TABLE brand (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(30) NOT NULL, 
	UNIQUE (name)
);

CREATE TABLE brand2 (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(30) NOT NULL, 
	UNIQUE (name)
);





CREATE TABLE customer_order2 (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	invoice VARCHAR(20) NOT NULL, 
	status VARCHAR(20) NOT NULL, 
	customer_id INTEGER NOT NULL, 
	date_created DATETIME NOT NULL, 
	orders TEXT, 
	UNIQUE (invoice)
);

CREATE TABLE user (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(50) NOT NULL, 
	username VARCHAR(80) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	password VARCHAR(180) NOT NULL, 
	profile VARCHAR(180) NOT NULL, 
	UNIQUE (username), 
	UNIQUE (email)
);



--  //////////////// Quest Gaming /////////////////////////////////

CREATE table users(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(80) NOT NULL,
    Last_Name VARCHAR(80) NOT NULL,
    User_Password VARCHAR(80) NOT NULL,
    DOB VARCHAR(80) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Terms_and_Conditions VARCHAR(80) NOT NULL,
    Over_18 VARCHAR(80) NOT NULL,
    Privacy_Policy VARCHAR(80) NOT NULL,
    News_Letter VARCHAR(80) NOT NULL,
    Text_Email_Alert VARCHAR(80) NOT NULL,
    Card_Details VARCHAR(80) NOT NULL,
    Toatal_Earnings VARCHAR(80) NOT NULL,
    Games_played VARCHAR(80) NOT NULL,
    end_point VARCHAR(80) NOT NULL,
    Ranking VARCHAR(80) NOT NULL,
    Tournaments_enterd VARCHAR(80) NOT NULL,
    Games VARCHAR(80) NOT NULL,
    Team_Members VARCHAR(80) NOT NULL,
    Active_Tournaments VARCHAR(80) NOT NULL
);

CREATE table  tournaments_table(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Game_Name VARCHAR(80) NOT NULL,
    Game_Type VARCHAR(80) NOT NULL,
    Tournament_Title VARCHAR(80) NOT NULL,
    Prize_Pot VARCHAR(80) NOT NULL,
    Entery_Cost VARCHAR(100) NOT NULL,
    Maximum_Participants VARCHAR(80) NOT NULL,
    Minimum_Participants VARCHAR(80) NOT NULL,
    Enroled VARCHAR(80) NOT NULL,
    Platform VARCHAR(80) NOT NULL,
    Starting_Date VARCHAR(80) NOT NULL,
    Tournament_Time VARCHAR(80) NOT NULL,
    Details VARCHAR(80) NOT NULL,
    Ruled VARCHAR(80) NOT NULL,
    end_point VARCHAR(80) NOT NULL,
    Number_Of_Rounds VARCHAR(80) NOT NULL,
    Region VARCHAR(80) NOT NULL,
    Potential_Profit VARCHAR(80) NOT NULL
);

CREATE table  fortnite_Squads_battle_royal(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);

CREATE table  fortniteSquads(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);



CREATE table  Fifa_Squads(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);

CREATE table  CALL_OF_DUTY_TEAM_D(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);


CREATE table  FORTNITE_FREE_FOR_ALL(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);

CREATE table  FIFA_1V1(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);

CREATE table  CALL_OF_DUTY_FREE_FOR_ALL(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);

CREATE table  FORTNITE_FREE_FOR_ALL_PS5_PRIZE(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);

CREATE table  FORTNITE_FREE_FOR_ALL_XBOX_SERIES_X_PRIZE(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Participant_User_Id VARCHAR(80) NOT NULL,
    Participant_State VARCHAR(80) NOT NULL,
    Gamertag_PC VARCHAR(80) NOT NULL,
    Gamertag_XBOX VARCHAR(80) NOT NULL,
    Gamertag_PS4 VARCHAR(100) NOT NULL,
    Team_member_1 VARCHAR(80) NOT NULL,
    Team_member_2 VARCHAR(80) NOT NULL,
    Team_member_3 VARCHAR(80) NOT NULL
);


INSERT INTO addproduct VALUES(1,'fortnite_battle_royal_solo','FORTNITE','BATTLE ROYAL','SOLO','Battle Royal Free For All',1000,1,512,100,1,'Cross Platform','31/07/2020','8:00','solo fortnite battle royal','FORTNITE | SOLO | BATTLE ROYAL','6','U.K','5120','0','fortnite',10,0,12,'Black, White','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fortnite.png','fortnite_logo.png','SOLOS-BANNER.png');
INSERT INTO addproduct VALUES(2,'fortnite_battle_royal_squads','FIFA','1V1','SOLO','1V1 KNOCK OUTS',1000,1,512,100,1,'PS4 XBOX','31/07/2020','8:00','solo fifa 1v1 knock outs','FIFA | SOLO | 1V1 KNOCK OUTS','6','U.K','5120','0','fortnite',10,0,12,'PS4, XBOX, P.C','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fifa.png','fifa_logo.png','SOLOS-BANNER.png');
INSERT INTO addproduct VALUES(3,'fifa_1V1_solo','CALL OF DUTY','DEATHMATCH','SOLO','FREE FOR ALL DEATHMATCH',1000,1,512,100,1,'Cross Platform','31/07/2020','8:00','solo fifa 1v1 knock outs','FIFA | SOLO | 1V1 KNOCK OUTS','6','U.K','5120','0','fortnite',10,0,12,'PS4, XBOX, P.C','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_cod.png','cod_logo.png','SOLOS-BANNER.png');

INSERT INTO addproduct VALUES(4,'fifa_2v2_duos','FORTNITE','BATTLE ROYAL','SQUADS','Battle Royal Free For All',1000,1,512,100,1,'Cross Platform','31/07/2020','8:00','solo fortnite battle royal','FORTNITE | SOLO | BATTLE ROYAL','6','U.K','5120','0','fortnite',10,0,12,'Black, White','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fortnite.png','fortnite_logo.png','SQUADS-BANNER.png');
INSERT INTO addproduct VALUES(5,'cod_team_death_match_squads','FIFA','1V1','DUO','2V2 KNOCK OUTS',1000,1,512,100,1,'PS4 XBOX','31/07/2020','8:00','solo fifa 1v1 knock outs','FIFA | SOLO | 1V1 KNOCK OUTS','6','U.K','5120','0','fortnite',10,0,12,'PS4, XBOX, P.C','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fifa.png','fifa_logo.png','SQUADS-BANNER.png');
INSERT INTO addproduct VALUES(6,'cod_team_death_match_solo','CALL OF DUTY','DEATHMATCH','SQUADS','FREE FOR ALL DEATHMATCH',1000,1,512,100,1,'Cross Platform','31/07/2020','8:00','solo fifa 1v1 knock outs','FIFA | SOLO | 1V1 KNOCK OUTS','6','U.K','5120','0','fortnite',10,0,12,'PS4, XBOX, P.C','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_cod.png','cod_logo.png','SQUADS-BANNER.png');

INSERT INTO addproduct VALUES(7,'fortnite_battle_royal_solo_ps5','FORTNITE','BATTLE ROYAL','SOLO','Battle Royal Free For All',1000,1,512,100,1,'Cross Platform','31/07/2020','8:00','solo fortnite battle royal','FORTNITE | SOLO | BATTLE ROYAL','6','U.K','5120','0','fortnite',10,0,12,'Black, White','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fortnite.png','fortnite_logo.png','SOLOS-BANNER.png');
INSERT INTO addproduct VALUES(8,'fortnite_battle_royal_solo_xboxX','FORTNITE','BATTLE ROYAL','SOLO','Battle Royal Free For All',1000,1,512,100,1,'Cross Platform','31/07/2020','8:00','solo fortnite battle royal','FORTNITE | SOLO | BATTLE ROYAL','6','U.K','5120','0','fortnite',10,0,12,'Black, White','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fortnite.png','fortnite_logo.png','SOLOS-BANNER.png');


-- INSERT INTO addproduct VALUES(2,'FIFA | 1V1',10,0,12,'Black, White','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fifa.png','fifa_logo.png','SOLOS-BANNER.png');
-- INSERT INTO addproduct VALUES(3,'CALL OF DUTY | TEAM DEATHMATCH',10,0,12,'Black, White ','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_cod.png','cod_logo.png','SOLOS-BANNER.png');
-- INSERT INTO addproduct VALUES(4,'FORTNITE | TEAM BATTLE ROYAL',10,0,12,'Black, White ','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fortnite.png','fortnite_logo.png','SQUADS-BANNER.png');
-- INSERT INTO addproduct VALUES(5,'FIFA | 2V2',10,0,12,'Black, White ','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fifa.png','fifa_logo.png','SQUADS-BANNER.png');
-- INSERT INTO addproduct VALUES(6,'CALL OF DUTY | F FREEOR ALL',10,0,12,'Black, White ','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_cod.png','cod_logo.png','SQUADS-BANNER.png');
-- INSERT INTO addproduct VALUES(7,'FORTNITE | BATTLE ROYAL WINNER TAKES ALL',10,0,12,'Black, White ','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fortnite.png','fortnite_logo.png','SOLOS-BANNER.png');
-- INSERT INTO addproduct VALUES(8,'FORTNITE | BATTLE ROYAL WINNER TAKES ALL',10,0,12,'Black, White ','S',replace(replace('With a mid-thigh length, this essential bodysuit holds in your core, shapes and lifts your butt and chest, and smooths your upper thighs. Its whisper-soft and seamless construction makes this sculpting piece a necessity for enhancing your body'' natural shape.\r\n\r\nIf you prefer more comfort for everyday wear, we recommend selecting a size up.\r\n\r\nFull Back, High-Cut Leg, Seamless Construction\r\nSherica Is Size 4 And 5''9", Wearing SKIMS S/M\r\n78% Nylon / 22% Spandex\r\nMachine Wash Cold, Do Not Bleach\r\nImported','\r',char(13)),'\n',char(10)),'2020-06-10 13:54:15.135792',1,1,'single_shots_fortnite.png','fortnite_logo.png','SOLOS-BANNER.png');


INSERT INTO fortnite_Squads_battle_royal VALUES(1,1,'in','SonOfKingstone','SonOfKingstone','SonOfKingstone','SonOfKingstone','SonOfKingstone','SonOfKingstone');
INSERT INTO fortnite_Squads_battle_royal VALUES(2,1,'in','GodsLeftNut','GodsLeftNut','GodsLeftNut','GodsLeftNut','GodsLeftNut','GodsLeftNut');


INSERT INTO fortniteSquads VALUES(1,1,'in','SonOfKingstone','SonOfKingstone','SonOfKingstone','SonOfKingstone','SonOfKingstone','SonOfKingstone');
INSERT INTO fortniteSquads VALUES(2,1,'in','GodsLeftNut','GodsLeftNut','GodsLeftNut','GodsLeftNut','GodsLeftNut','GodsLeftNut');


INSERT INTO brand2 VALUES(2,'SDFSDFDSF');

-- INSERT INTO register VALUES(1,'Tino Mushangwe','SonOfKingstone','tinokingstone@gmail.com',X'24326224313224515a536367654c4f704c716e5234674c493143656465464345616d414e4e51334546697a734a73527a50775161576b4c4443574c61','United Kingdom','Sunderland','07951977769','8 Benton Avenue','SR5 4NB','profile.jpg','2020-05-29 15:41:11.050085');

-- INSERT INTO customer_order VALUES(1,'77978e67da','Pending',1,'2020-05-16 10:39:49.160346','{"5": {"color": "Black", "colors": "Black, White ", "discount": 25, "image": "8d9bc7b8236bb17b8453.png", "name": "Sony Bravia TV ", "price": 1000.0, "quantity": 1}, "6": {"color": "Black", "colors": "Black, White ", "discount": 25, "image": "7f5d77a16d56e7827678.png", "name": "Samsung TV", "price": 1800.0, "quantity": 2}}');

COMMIT;