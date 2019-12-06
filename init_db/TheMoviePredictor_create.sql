CREATE TABLE `movies` (
	`id` int NOT NULL AUTO_INCREMENT,
	`title` varchar(255) NOT NULL,
	`imdb_id` varchar(20) UNIQUE KEY,
	`original_title` varchar(255) DEFAULT NULL,
	`synopsis` TEXT DEFAULT NULL,
	`duration` int NOT NULL,
	`rating` enum('TP', '-12', '-16', '-18') DEFAULT NULL,
	`production_budget` int DEFAULT NULL,
	`marketing_budget` int DEFAULT NULL,
	`release_date` DATE DEFAULT NULL,
	`is_3d` bool NOT NULL DEFAULT '0',
	`origin_country` char(2) DEFAULT NULL,
	`actors` varchar(255) DEFAULT NULL,
	`productors` varchar(255) DEFAULT NULL,
	`directors` varchar(255) DEFAULT NULL,
	`public_note` FLOAT DEFAULT NULL,
	`public_votes` INT DEFAULT NULL,
	`press_note` FLOAT DEFAULT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `people` (
	`id` int NOT NULL AUTO_INCREMENT,
	`imdb_id` varchar(20) UNIQUE KEY NULL,
	`firstname` varchar(255) NOT NULL,
	`lastname` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

INSERT INTO `movies` 
    (`title`, `original_title`, `imdb_id`, `duration`, `rating`, `release_date`)
VALUES
    ('Joker', 'Joker', 'test', 122, '-12', '2019-10-09'),
    ('Joker2', 'blabla', 'test2', 146, '-12', '2018-05-04')
;

INSERT INTO `people`
    (`firstname`, `lastname`)
VALUES
    ('Joaquin', 'Phoenix'),
    ('Todd', 'Phillips'),
    ('Scott', 'Silver')
;