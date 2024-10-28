create database DBDA1;

use  DBDA;


create table test (
personname varchar(50),
 age int);
 
 
 CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

insert into trial values ('vas', 12, '2024-09-23');


alter table test add  Bday DATE; 

set SQL_SAFE_UPDATES=0;

truncate table trial;

rename table test to trial;


select * from trial;

describe trial;

update trial set age = 200;


SHOW ENGINE INNODB STATUS;





-- 1. Create a sample database
CREATE DATABASE SampleDB;
USE SampleDB;

-- 2. Create tables

-- Create table for departments
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    DepartmentName VARCHAR(50) NOT NULL
);

-- Create table for employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DepartmentID INT,
    Salary DECIMAL(10, 2),
    HireDate DATE,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Create table for projects
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectName VARCHAR(100) NOT NULL,
    StartDate DATE,
    EndDate DATE
);

-- Create table for Employee-Project assignments (many-to-many relationship)
CREATE TABLE EmployeeProjects (
    EmployeeID INT,
    ProjectID INT,
    Role VARCHAR(50),
    PRIMARY KEY (EmployeeID, ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- 3. Insert data into Departments table
INSERT INTO Departments (DepartmentName) VALUES 
('HR'), 
('Engineering'), 
('Sales');

-- 4. Insert data into Employees table
INSERT INTO Employees (FirstName, LastName, DepartmentID, Salary, HireDate) VALUES
('John', 'Doe', 2, 75000, '2020-05-15'),
('Jane', 'Smith', 1, 60000, '2019-03-01'),
('Mike', 'Brown', 3, 55000, '2021-07-11'),
('Emily', 'Davis', 2, 80000, '2018-10-20');

-- 5. Insert data into Projects table
INSERT INTO Projects (ProjectName, StartDate, EndDate) VALUES
('Website Redesign', '2023-01-10', '2023-06-15'),
('Mobile App Development', '2022-04-01', '2022-12-20'),
('Sales Platform Overhaul', '2023-02-01', NULL);

-- 6. Insert data into EmployeeProjects table
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, Role) VALUES
(1, 1, 'Frontend Developer'),
(4, 1, 'Backend Developer'),
(2, 2, 'Project Manager'),
(3, 3, 'Sales Consultant');

-- 7. Practice SQL Queries

-- a. SELECT query
SELECT * FROM Employees;

-- b. INNER JOIN query to see employees with their department names
SELECT E.FirstName, E.LastName, D.DepartmentName, E.Salary
FROM Employees E
JOIN Departments D ON E.DepartmentID = D.DepartmentID;

-- c. LEFT JOIN query to see all projects and their assigned employees
SELECT P.ProjectName, E.FirstName, E.LastName
FROM Projects P
LEFT JOIN EmployeeProjects EP ON P.ProjectID = EP.ProjectID
LEFT JOIN Employees E ON EP.EmployeeID = E.EmployeeID;

-- d. UPDATE salary of an employee
UPDATE Employees
SET Salary = Salary + 5000
WHERE EmployeeID = 1;

-- e. DELETE an employee
DELETE FROM Employees
WHERE EmployeeID = 3;

-- f. Add a new project
INSERT INTO Projects (ProjectName, StartDate, EndDate) VALUES
('AI Research Project', '2024-01-15', NULL);

-- g. Subquery example to get employees with salaries greater than the average
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);


View > Output Area;

