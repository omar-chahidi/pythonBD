DROP DATABASE IF EXISTS `datatest`;
CREATE DATABASE IF NOT EXISTS `datatest`;
USE  `datatest`;

/*
Création des tables
*/

CREATE TABLE IF NOT EXISTS `ninjatable`
(
	`id_ninja` INT NOT NULL AUTO_INCREMENT,
    `ninja_firstnam` VARCHAR(30) NOT NULL UNIQUE,
    `ninja_lastname` VARCHAR(500) NOT NULL,
    PRIMARY KEY(`id_ninja`)
);

/*
Ajouter de quelques enregistrements
*/

INSERT INTO `ninjatable`(`ninja_firstnam`, `ninja_lastname`)
VALUES
('oci', 'omar'),
('cbu', 'christophe'),
('cgo', 'cyril');