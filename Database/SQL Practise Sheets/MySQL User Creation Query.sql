# MySQL: CREATE USER statement


CREATE USER
  'mike'@'localhost' IDENTIFIED BY 'cdac';
  
  
# Create more than one user:

CREATE USER
  'mike'@'localhost' IDENTIFIED BY 'ceit',
  'Andy'@'localhost' IDENTIFIED BY 'png';
  
  
# MySQL: Change a user password:

SET PASSWORD FOR 'mike'@'localhost' = 'abc';


# MySQL: RENAME USER statement

RENAME USER
  'mike'@'localhost' TO 'John'@'localhost';
  
  
# Rename more than one user:

RENAME USER
  'John'@'localhost' TO 'mike'@'localhost',
  'Andy'@'localhost' TO 'Will'@'localhost';
  
  
# MySQL: DROP USER statement:

DROP USER 'mike'@'localhost';

#Drop more than one user:

DROP USER 'mike'@'localhost', 'Will'@'localhost';


# MySQL: Find Users:

SELECT User
FROM mysql.user;




# MySQL: Grant privileges:



