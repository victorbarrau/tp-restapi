CREATE TABLE USER
(
    ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    firstname Varchar(50),
    lastname Varchar(50),
    age int,
    email Varchar(250),
    job Varchar(50)
)
;
CREATE TABLE APPLICATION
(
    ID int,
    appname Varchar(50),
    username Varchar(50),
    lastconection DATE,
    email Varchar(250),
    FOREIGN KEY(userid) REFERENCES USER(id)
);