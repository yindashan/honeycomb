DROP TABLE IF EXISTS `number`;
CREATE TABLE `number` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serial_number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `serial_number` (`serial_number`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

insert into number values(1,1);


DROP TABLE IF EXISTS `version`;
CREATE TABLE `version` (
  `version` varchar(10) NOT NULL
);

insert into version values('0.0.1');

