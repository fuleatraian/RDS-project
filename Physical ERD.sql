CREATE TABLE `country`(
    `country_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `country_name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `country` ADD PRIMARY KEY `country_country_id_primary`(`country_id`);
CREATE TABLE `city`(
    `city_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `city_name` VARCHAR(255) NOT NULL,
    `country_id` INT NOT NULL
);
ALTER TABLE
    `city` ADD PRIMARY KEY `city_city_id_primary`(`city_id`);
CREATE TABLE `department`(
    `dept_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `dept_name` VARCHAR(255) NOT NULL,
    `city_id` INT NOT NULL
);
ALTER TABLE
    `department` ADD PRIMARY KEY `department_dept_id_primary`(`dept_id`);
CREATE TABLE `empoyees`(
    `dept_id` INT NOT NULL,
    `emp_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255) NOT NULL,
    `second_name` VARCHAR(255) NOT NULL,
    `gender` VARCHAR(255) NOT NULL,
    `age` INT NOT NULL,
    `hire_date` DATE NOT NULL
);
ALTER TABLE
    `empoyees` ADD PRIMARY KEY `empoyees_emp_id_primary`(`emp_id`);
CREATE TABLE `area`(
    `area_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `area_postcode` VARCHAR(255) NOT NULL,
    `city_id` INT NOT NULL
);
ALTER TABLE
    `area` ADD PRIMARY KEY `area_area_id_primary`(`area_id`);
CREATE TABLE `sales_chief`(
    `emp_id` INT NOT NULL,
    `performance` VARCHAR(255) NOT NULL,
    `target` VARCHAR(255) NOT NULL,
    `area_id` INT NOT NULL,
    `rep_id` INT NOT NULL
);
ALTER TABLE
    `sales_chief` ADD PRIMARY KEY `sales_chief_emp_id_primary`(`emp_id`);
ALTER TABLE
    `sales_chief` ADD PRIMARY KEY `sales_chief_area_id_primary`(`area_id`);
CREATE TABLE `sales_supervisor`(
    `emp_id` INT NOT NULL,
    `experience` INT NOT NULL
);
ALTER TABLE
    `sales_supervisor` ADD PRIMARY KEY `sales_supervisor_emp_id_primary`(`emp_id`);
CREATE TABLE `team`(
    `emp_id` INT NOT NULL,
    `team_id` INT UNSIGNED NOT NULL AUTO_INCREMENT
);
ALTER TABLE
    `team` ADD PRIMARY KEY `team_team_id_primary`(`team_id`);
CREATE TABLE `property`(
    `prop_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `area_id` INT NOT NULL,
    `type_id` INT NOT NULL,
    `no_bed` INT NOT NULL,
    `no_bath` INT NOT NULL,
    `price` INT NOT NULL,
    `status_id` INT NOT NULL,
    `emp_id` INT NOT NULL
);
ALTER TABLE
    `property` ADD PRIMARY KEY `property_prop_id_primary`(`prop_id`);
CREATE TABLE `sales_rep`(
    `emp_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `team_id` INT NOT NULL,
    `active_negot` INT NOT NULL,
    `specialization` ENUM('') NOT NULL
);
ALTER TABLE
    `sales_rep` ADD PRIMARY KEY `sales_rep_emp_id_primary`(`emp_id`);
CREATE TABLE `customer`(
    `custom_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `budget` INT NOT NULL,
    `intention` VARCHAR(255) NOT NULL,
    `emp_id` INT NOT NULL
);
ALTER TABLE
    `customer` ADD PRIMARY KEY `customer_custom_id_primary`(`custom_id`);
CREATE TABLE `property_type`(
    `type_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `type_name` INT NOT NULL
);
ALTER TABLE
    `property_type` ADD PRIMARY KEY `property_type_type_id_primary`(`type_id`);
CREATE TABLE `property_status`(
    `status_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `status_name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `property_status` ADD PRIMARY KEY `property_status_status_id_primary`(`status_id`);
CREATE TABLE `report_dept`(
    `rep_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `rep_name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `report_dept` ADD PRIMARY KEY `report_dept_rep_id_primary`(`rep_id`);
ALTER TABLE
    `department` ADD CONSTRAINT `department_city_id_foreign` FOREIGN KEY(`city_id`) REFERENCES `city`(`city_id`);
ALTER TABLE
    `city` ADD CONSTRAINT `city_country_id_foreign` FOREIGN KEY(`country_id`) REFERENCES `country`(`country_id`);
ALTER TABLE
    `empoyees` ADD CONSTRAINT `empoyees_dept_id_foreign` FOREIGN KEY(`dept_id`) REFERENCES `department`(`dept_id`);
ALTER TABLE
    `sales_chief` ADD CONSTRAINT `sales_chief_rep_id_foreign` FOREIGN KEY(`rep_id`) REFERENCES `report_dept`(`rep_id`);
ALTER TABLE
    `property` ADD CONSTRAINT `property_area_id_foreign` FOREIGN KEY(`area_id`) REFERENCES `area`(`area_id`);
ALTER TABLE
    `area` ADD CONSTRAINT `area_city_id_foreign` FOREIGN KEY(`city_id`) REFERENCES `city`(`city_id`);
ALTER TABLE
    `sales_rep` ADD CONSTRAINT `sales_rep_team_id_foreign` FOREIGN KEY(`team_id`) REFERENCES `team`(`team_id`);
ALTER TABLE
    `team` ADD CONSTRAINT `team_emp_id_foreign` FOREIGN KEY(`emp_id`) REFERENCES `sales_supervisor`(`emp_id`);
ALTER TABLE
    `property` ADD CONSTRAINT `property_emp_id_foreign` FOREIGN KEY(`emp_id`) REFERENCES `sales_rep`(`emp_id`);
ALTER TABLE
    `customer` ADD CONSTRAINT `customer_emp_id_foreign` FOREIGN KEY(`emp_id`) REFERENCES `sales_rep`(`emp_id`);
ALTER TABLE
    `property` ADD CONSTRAINT `property_type_id_foreign` FOREIGN KEY(`type_id`) REFERENCES `property_type`(`type_id`);
ALTER TABLE
    `property` ADD CONSTRAINT `property_status_id_foreign` FOREIGN KEY(`status_id`) REFERENCES `property_status`(`status_id`);