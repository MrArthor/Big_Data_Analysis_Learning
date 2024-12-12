SELECT user FROM mysql.user;
create database Dept;
create database Emp;






-- 1. Create user and implement the following commands on relation (Emp and Dept).

CREATE USER 'VanshSachdeva'@'localhost' IDENTIFIED BY '123456';

-- 2. Develop a query to grant all privileges of employees table into departments table.

GRANT ALL PRIVILEGES ON Emp TO 'VanshSachdeva'@'localhost';
GRANT ALL PRIVILEGES ON Dept TO 'VanshSachdeva'@'localhost';
SHOW GRANTS FOR 'VanshSachdeva'@'localhost';

-- 3. Develop a query to grant some privileges of employees table into departments table.

GRANT SELECT, INSERT, UPDATE ON Emp TO 'VanshSachdeva'@'localhost';
GRANT SELECT, INSERT, UPDATE ON Dept TO 'VanshSachdeva'@'localhost';
SHOW GRANTS FOR 'VanshSachdeva'@'localhost';

-- 4. Develop a query to revoke all privileges of employees table from departments table.

REVOKE ALL PRIVILEGES ON Emp FROM 'VanshSachdeva'@'localhost';
REVOKE ALL PRIVILEGES ON Dept FROM 'VanshSachdeva'@'localhost';
SHOW GRANTS FOR 'VanshSachdeva'@'localhost';

-- 5. Develop a query to revoke some privileges of employees table from departments table.

REVOKE SELECT, INSERT ON Emp FROM 'VanshSachdeva'@'localhost';
REVOKE SELECT, INSERT ON Dept FROM 'VanshSachdeva'@'localhost';
SHOW GRANTS FOR 'VanshSachdeva'@'localhost';
