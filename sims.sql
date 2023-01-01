CREATE SCHEMA `sims` ;
CREATE TABLE `new_schema`.`students` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `matric_no` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(45) NULL,
  `dob` VARCHAR(45) NULL,
  `faculty` VARCHAR(45) NULL,
  `department` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
SELECT * FROM sims.students;