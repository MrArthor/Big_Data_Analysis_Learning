create database assignment2;
use assignment2;

-- Question 1
-- 1. Create the EMPLOYEE table
CREATE TABLE EMPLOYEE (
    Emp_no INT PRIMARY KEY,
    E_name VARCHAR(255),
    E_address VARCHAR(255),
    E_ph_no VARCHAR(15),
    Dept_no INT,
    Dept_name VARCHAR(255),
    Job_id CHAR(10),
    Salary DECIMAL(10, 2)
);

-- 2. Add a new column HIREDATE to the existing relation
ALTER TABLE EMPLOYEE 
ADD HIREDATE DATE;

-- 3. Change the datatype of JOB_ID from CHAR to VARCHAR2
ALTER TABLE EMPLOYEE 
MODIFY Job_id VARCHAR(10);

-- 4. Change the name of column Emp_no to E_no
ALTER TABLE EMPLOYEE 
RENAME COLUMN Emp_no TO E_no;

-- 5. Modify the column width of the Job_id field
ALTER TABLE EMPLOYEE 
MODIFY Job_id VARCHAR(20);


-- Question 2

-- 1. Create the EMPLOYEE table
CREATE TABLE EMPLOYE (
    Emp_no INT PRIMARY KEY,
    E_name VARCHAR(255),
    E_address VARCHAR(255),
    E_ph_no VARCHAR(15),
    Dept_no VARCHAR(10),
    Dept_name VARCHAR(255),
    Job_id VARCHAR(10),
    Salary DECIMAL(10, 2)
);

-- 2. Insert at least 5 rows into the EMPLOYEE table with Indian names and locations
INSERT INTO EMPLOYE (Emp_no, E_name, E_address, E_ph_no, Dept_no, Dept_name, Job_id, Salary)
VALUES 
(11, 'Amit', 'Mumbai', '9876543210', 'D10', 'HR', 'J01', 50000),
(12, 'Sita', 'Delhi', '9123456789', 'D10', 'SALES', 'J02', 60000),
(13, 'Ravi', 'Bangalore', '9223344556', 'D20', 'MECH', 'J03', 70000),
(14, 'Kiran', 'Chennai', '9876543211', 'D30', 'IT', 'J04', 80000),
(15, 'Geeta', 'Kolkata', '9456781234', 'D10', 'SALES', 'J05', 55000);

-- 3. Display all the information of EMPLOYEE table
SELECT * FROM EMPLOYE;

-- 4. Display the record of each employee who works in department D10
SELECT * FROM EMPLOYE WHERE Dept_no = 'D10';

-- 5. Update the city of Emp_no 12 to Nagpur
UPDATE EMPLOYE SET E_address = 'Nagpur' WHERE Emp_no = 12;

-- 6. Display the details of Employee who works in department MECH
SELECT * FROM EMPLOYE WHERE Dept_name = 'MECH';

-- 7. Delete the E_ph_no (phone number) of employee Ravi
UPDATE EMPLOYE SET E_ph_no = NULL WHERE E_name = 'Ravi';

-- 8. Display the complete record of employees working in SALES Department
SELECT 
    *
FROM
    EMPLOYE
WHERE
    Dept_name = 'SALES'-- 1. List the E_no, E_name, Salary of all employees working for MANAGER.
SELECT E_no, E_name, Salary 
FROM EMPLOYEE 
WHERE Job_id = 'MANAGER';

-- 2. Display all the details of the employee whose salary is more than the salary of any IT PROFF.
SELECT * 
FROM EMPLOYEE 
WHERE Salary > (SELECT MAX(Salary) FROM EMPLOYEE WHERE Job_id = 'IT PROFF');

-- 3. List the employees in the ascending order of Designations of those who joined after 1981.
SELECT * 
FROM EMPLOYEE 
WHERE HIREDATE > '1981-12-31' 
ORDER BY Job_id ASC;

-- 4. List the employees along with their Experience and Daily Salary.
SELECT E_name, 
       (YEAR(CURDATE()) - YEAR(HIREDATE)) AS Experience, 
       (Salary / 30) AS Daily_Salary 
FROM EMPLOYEE;

-- 5. List the employees who are either ‘CLERK’ or ‘ANALYST’.
SELECT * 
FROM EMPLOYEE 
WHERE Job_id IN ('CLERK', 'ANALYST');

-- 6. List the employees who joined on 1-MAY-81, 3-DEC-81, 17-DEC-81, 19-JAN-80.
SELECT * 
FROM EMPLOYEE 
WHERE HIREDATE IN ('1981-05-01', '1981-12-03', '1981-12-17', '1980-01-19');

-- 7. List the employees who are working for the Deptno 10 or 20.
SELECT * 
FROM EMPLOYEE 
WHERE Dept_no IN ('10', '20');

-- 8. List the E_names that are starting with ‘S’.
SELECT E_name 
FROM EMPLOYEE 
WHERE E_name LIKE 'S%';

-- 9. Display the name as well as the first five characters of name(s) starting with ‘H’.
SELECT E_name, LEFT(E_name, 5) AS First_Five_Chars 
FROM EMPLOYEE 
WHERE E_name LIKE 'H%';

-- 10. List all the employees except ‘PRESIDENT’ & ‘MGR’ in ascending order of Salaries.
SELECT * 
FROM EMPLOYEE 
WHERE Job_id NOT IN ('PRESIDENT', 'MGR') 
ORDER BY Salary ASC;



-- Question 3 

-- 1. List the E_no, E_name, Salary of all employees working for MANAGER.
SELECT E_no, E_name, Salary 
FROM EMPLOYEE 
WHERE Job_id = 'MANAGER';

-- 2. Display all the details of the employee whose salary is more than the salary of any IT PROFF.
SELECT * 
FROM EMPLOYEE 
WHERE Salary > (SELECT MAX(Salary) FROM EMPLOYEE WHERE Job_id = 'IT PROFF');

-- 3. List the employees in the ascending order of Designations of those who joined after 1981.
SELECT * 
FROM EMPLOYEE 
WHERE HIREDATE > '1981-12-31' 
ORDER BY Job_id ASC;

-- 4. List the employees along with their Experience and Daily Salary.
SELECT E_name, 
       (YEAR(CURDATE()) - YEAR(HIREDATE)) AS Experience, 
       (Salary / 30) AS Daily_Salary 
FROM EMPLOYEE;

-- 5. List the employees who are either ‘CLERK’ or ‘ANALYST’.
SELECT * 
FROM EMPLOYEE 
WHERE Job_id IN ('CLERK', 'ANALYST');

-- 6. List the employees who joined on 1-MAY-81, 3-DEC-81, 17-DEC-81, 19-JAN-80.
SELECT * 
FROM EMPLOYEE 
WHERE HIREDATE IN ('1981-05-01', '1981-12-03', '1981-12-17', '1980-01-19');

-- 7. List the employees who are working for the Deptno 10 or 20.
SELECT * 
FROM EMPLOYEE 
WHERE Dept_no IN ('10', '20');

-- 8. List the E_names that are starting with ‘S’.
SELECT E_name 
FROM EMPLOYEE 
WHERE E_name LIKE 'S%';

-- 9. Display the name as well as the first five characters of name(s) starting with ‘H’.
SELECT E_name, LEFT(E_name, 5) AS First_Five_Chars 
FROM EMPLOYEE 
WHERE E_name LIKE 'H%';

-- 10. List all the employees except ‘PRESIDENT’ & ‘MGR’ in ascending order of Salaries.
SELECT * 
FROM EMPLOYEE 
WHERE Job_id NOT IN ('PRESIDENT', 'MGR') 
ORDER BY Salary ASC;


