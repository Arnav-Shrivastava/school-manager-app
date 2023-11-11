
USE TIMETABLE;


CREATE TABLE FACULTY(
    FID int PRIMARY KEY,
    PASSWORD varchar(50),
    NAME varchar(50),
    INITIAL varchar(50),
    EMAIL varchar (50),
    SUBCODE1 varchar (50),
    SUBCODE2 varchar (50));

CREATE TABLE SCHEDULE(
    ID varchar(5) PRIMARY KEY,
    DAYID int,
    PERIODID int,
    SUBCODE varchar(50),
    SECTION varchar(50),
    INITIAL varchar(50));

CREATE TABLE STUDENT(
    ADMISSION_ID int PRIMARY KEY,
    PASSWORD varchar(50),
    NAME varchar(50),
    ROLL int,
    SECTION varchar(50));

CREATE TABLE SUBJECT(
    SUBCODE varchar(50) PRIMARY KEY,
    SUBNAME varchar(50),
    SUBTYPE varchar(50));


CREATE TABLE SUBJECT(SUBCODE CHAR(10) NOT NULL PRIMARY KEY,
    SUBNAME CHAR(50) NOT NULL,
    SUBTYPE CHAR(1) NOT NULL);