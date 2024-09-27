CREATE DATABASE telefonkatalog;
USE telefonkatalog;

CREATE TABLE person (
    id INT NOT NULL AUTO_INCREMENT,
    fornavn VARCHAR(255) NOT NULL,
    etternavn VARCHAR(255) NOT NULL,
    telefonnummer CHAR(8),
    PRIMARY KEY (id)
);
