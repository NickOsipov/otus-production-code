CREATE DATABASE IF NOT EXISTS `machine_learning`;

USE `machine_learning`;

CREATE TABLE IF NOT EXISTS `predictions` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `sepal_length` FLOAT NOT NULL,
    `sepal_width` FLOAT NOT NULL,
    `petal_length` FLOAT NOT NULL,
    `petal_width` FLOAT NOT NULL,
    `predicted_class` VARCHAR(255) NOT NULL,
    `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;