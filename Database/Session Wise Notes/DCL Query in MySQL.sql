/*
To perform DML operations on a table permissions are required and are called Privileges. These privileges can be controlled efficiently by using MySQL DCL statements.
MySQL Data Control Language is similar to SQL Data Control Language and these are classified into two types:

1.) GRANT
2.) REVOKE

GRANT:	Grant is used to grant permissions to the clients.
In the MySQL database, it offers both the server and client a great amount of control privileges.

Syntax:
			GRANT { ALL | statement [ ,…n ] }
			TO security_account [ ,…n ]
            
REVOKE:  The revoke command will cancel all the permissions from the user.

Syntax:		REVOKE
			<priv_type> [<column_list>]
			[ priv_type [<column_list>]] …
			ON [object_type] priv_level
			FROM user [user] …
			REVOKE ALL PRIVILEGES, GRANT OPTION
			FROM user [ user] …

1.) To perform DML operation on a table, 
permissions are required those permissions are called as privileges.
2.)Grant – Grant  permissions to users.
3.) Revoke – Revoke permissions from users.
*/


# MySQL: CREATE USER statement


CREATE USER
  'mike'@'localhost' IDENTIFIED BY 'ceit';
  
  
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


# MySQL: Find Users logged:

SELECT SUBSTRING_INDEX(host, ':', 1) AS host_short,
       GROUP_CONCAT(DISTINCT user) AS users,
       COUNT(*) AS threads
FROM information_schema.processlist
GROUP BY host_short
ORDER BY COUNT(*), host_short;


# MySQL: Grant privileges:

SHOW GRANTS FOR 'mike'@'localhost';

-- OUTPUT: 
-- 'GRANT USAGE ON *.* TO `mike`@`localhost`'
-- Here, the USAGE means a user can log in to the database but does not have any privileges.



GRANT ALL PRIVILEGES ON world.city TO 'mike'@'localhost';

GRANT SELECT ON world.city to 'mike'@'localhost';


GRANT ALL PRIVILEGES ON world.country TO 'mike'@'localhost' WITH GRANT OPTION;


GRANT ALL PRIVILEGES ON world.employee TO 'mike'@'localhost';


GRANT SELECT (Name), INSERT (Name, CountryCode), UPDATE (Name,CountryCode)
ON world.city TO 'mike'@'localhost';


REVOKE ALL, GRANT OPTION FROM 'mike'@'localhost';  


REVOKE UPDATE, INSERT ON world.* FROM 'mike'@'localhost';  


REVOKE SELECT (Name), INSERT (Name, CountryCode), UPDATE (Name,CountryCode)
ON world.city TO 'mike'@'localhost';

