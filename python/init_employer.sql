DROP TABLE employer;
CREATE TABLE employer
(
reference BIGINT AUTO_INCREMENT,
firstName VARCHAR(50),
lastName VARCHAR(50),
username VARCHAR(25),
password VARCHAR(100),
email VARCHAR(30),
phoneNumber INT,
address VARCHAR(100),
PRIMARY KEY (reference)
);