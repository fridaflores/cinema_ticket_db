#Data Base for buying a ticket in a movie theater

CREATE DATABASE IF NOT EXISTS cinema_ticket_db;
USE cinema_ticket_db;

CREATE TABLE IF NOT EXISTS users
(
	id_user INT NOT NULL auto_increment,
	type_user VARCHAR(10) NOT NULL,
    PRIMARY KEY(id_user)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS admin_u
(
	id_ad INT NOT NULL auto_increment,
    id_user INT,
	u_fname VARCHAR(35) NOT NULL,
    u_sname1 VARCHAR(35) NOT NULL,
    u_sname2 VARCHAR(35),
    PRIMARY KEY(id_ad),
    CONSTRAINT fk_au FOREIGN KEY (id_user)
    REFERENCES users(id_user)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)ENGINE = INNODB;