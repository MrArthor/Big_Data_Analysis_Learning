/*
The AUTOCOMMIT variable is set true by default. 
This can be changed in the following way,
*/
-- To make autcommit false
SET AUTOCOMMIT=false;
-- or
SET AUTOCOMMIT=0;

-- To make autcommit true
SET AUTOCOMMIT=true;
-- or
SET AUTOCOMMIT=1;

-- To view AUTOCOMMIT status
 
SELECT @@autocommit;

-- COMMIT
/*
If AUTOCOMMIT set to false and the transaction not committed, the changes will be visible only for the current connection.

After COMMIT statement commits the changes to the table, the result will be visible for all connections.

We consider two connections to explain this

*/

-- Connection 1

-- Before making autocommit false one row added in a new table
INSERT INTO testTable VALUES (1);

-- Making autocommit = false
SET autocommit=0;

INSERT INTO testTable VALUES (2), (3);    
SELECT * FROM testTable;

/*
+-----+
| tId |
+-----+
|   1 |
|   2 |
|   3 |
+-----+

*/

-- Connection 2

SELECT * FROM testTable;

/*
+-----+
| tId |
+-----+
|   1 |
+-----+
*/
-- Row inserted before autocommit=false only visible here

-- Connection 1

COMMIT;
-- Now COMMIT is executed in connection 1
SELECT * FROM testTable;

/*
    +-----+
    | tId |
    +-----+
    |   1 |
    |   2 |
    |   3 |
    +-----+
    
    */
    
-- Connection 2

SELECT * FROM testTable;

/*
    +-----+
    | tId |
    +-----+
    |   1 |
    |   2 |
    |   3 |
    +-----+
    
    */
-- Now all the three rows are visible here

-- -------------------- ROLLBACK ------------------------------- --

-- ROLLBACK

/*
If anything went wrong in your query execution, ROLLBACK in used to revert the changes. 
See the explanation below
*/
-- Before making autocommit false one row added in a new table
INSERT INTO testTable VALUES (1);

-- Making autocommit = false
SET autocommit=0;

INSERT INTO testTable VALUES (2), (3);    
SELECT * FROM testTable;
/*
+-----+
| tId |
+-----+
|   1 |
|   2 |
|   3 |
+-----+
*/
-- Now we are executing ROLLBACK

-- Rollback executed now
ROLLBACk;

SELECT * FROM testTable;

/*
+-----+
| tId |
+-----+
|   1 |
+-----+

*/
-- Rollback removed all rows which all are not committed
-- Once COMMIT is executed, then ROLLBACK will not cause anything

INSERT INTO testTable VALUES (2), (3);    
SELECT * FROM testTable;
COMMIT;

/*
+-----+
| tId |
+-----+
|   1 |
|   2 |
|   3 |
+-----+

*/

-- Rollback executed now
ROLLBACk;

SELECT * FROM testTable;

/*
+-----+
| tId |
+-----+
|   1 |
|   2 |
|   3 |
+-----+

*/
-- Rollback not removed any rows

-- If AUTOCOMMIT is set true, then COMMIT and ROLLBACK is useless



create table emp(
emp_id int not null,
emp_name varchar(25) not null,
salary decimal(8,2));


insert into emp values(1,'pankaj',125000);
select * from emp;

savepoint sp1;
insert into emp values(2,'Aditya',155000);


rollback to sp1;

ROLLBACK;

update emp set salary = salary+10000 
where emp_id = 1;

select * from emp;

commit;
rollback;

set autocommit = 0;

update emp set salary = salary+10000 
where emp_id = 1;
select * from emp;

commit;
rollback;

set autocommit = 1;

SELECT @@autocommit;