create database CDACACTS;
use CDACACTS;


-- Create the Sailors table
CREATE TABLE Sailors (
    sid INT PRIMARY KEY,
    sname VARCHAR(50),
    rating INT,
    age FLOAT
);

-- Insert values into the Sailors table
INSERT INTO Sailors (sid, sname, rating, age) VALUES
(22, 'Dustin', 7, 45),
(29, 'Brutus', 1, 33),
(31, 'Lubber', 8, 55.5),
(32, 'Andy', 8, 25.5),
(58, 'Rusty', 10, 35),
(64, 'Horatio', 7, 35),
(71, 'Zorba', 10, 16),
(74, 'Horatio', 9, 40),
(85, 'Art', 3, 25.5),
(95, 'Bob', 3, 63.5);

-- Create the Boats table
CREATE TABLE Boats (
    bid INT PRIMARY KEY,
    bname VARCHAR(50),
    color VARCHAR(20)
);

-- Insert values into the Boats table
INSERT INTO Boats (bid, bname, color) VALUES
(101, 'Interlake', 'blue'),
(102, 'Interlake', 'red'),
(103, 'Clipper', 'green'),
(104, 'Marine', 'red');

-- Create the Reserves table
CREATE TABLE Reserves (
    sid INT,
    bid INT,
    day DATE,
    PRIMARY KEY (sid, bid, day),
    FOREIGN KEY (sid) REFERENCES Sailors(sid),
    FOREIGN KEY (bid) REFERENCES Boats(bid)
);

-- Insert values into the Reserves table
INSERT INTO Reserves (sid, bid, day) VALUES
(22, 101, '1998-10-10'),
(22, 102, '1998-10-10'),
(22, 103, '1998-10-8'),
(22, 104, '1998-10-7'),
(31, 102, '1998-11-10'),
(31, 102, '1998-11-6'),
(31, 104, '1998-11-12'),
(64, 101, '1998-9-5'),
(64, 102, '1998-9-8'),
(74, 103, '1998-9-8');


-- 1. Find all information of sailors who have reserved boat number 101.
SELECT * 
FROM Sailors 
WHERE sid IN (
    SELECT sid 
    FROM Reserves 
    WHERE bid = 101
);

-- 2. Find the name of boat reserved by Bob.
SELECT bname 
FROM Boats 
WHERE bid IN (
    SELECT bid 
    FROM Reserves 
    WHERE sid = (SELECT sid FROM Sailors WHERE sname = 'Bob')
);

-- 3. Find the names of sailors who have reserved a red boat, and list in the order of age.
SELECT sname 
FROM Sailors 
WHERE sid IN (
    SELECT sid 
    FROM Reserves 
    WHERE bid IN (SELECT bid FROM Boats WHERE color = 'red')
)
ORDER BY age;

-- 4. Find the names of sailors who have reserved at least one boat.
SELECT sname 
FROM Sailors 
WHERE sid IN (
    SELECT DISTINCT sid 
    FROM Reserves
);

-- 5. Find the ids and names of sailors who have reserved two different boats on the same day.
SELECT sid, sname 
FROM Sailors 
WHERE sid IN (
    SELECT sid 
    FROM Reserves 
    GROUP BY sid, day 
    HAVING COUNT(DISTINCT bid) >= 2
);

-- 6. Find the ids of sailors who have reserved a red boat or a green boat.
SELECT DISTINCT sid 
FROM Reserves 
WHERE bid IN (
    SELECT bid 
    FROM Boats 
    WHERE color = 'red' OR color = 'green'
);

-- 7. Find the name and the age of the youngest sailor.
SELECT sname, age 
FROM Sailors 
WHERE age = (SELECT MIN(age) FROM Sailors);

-- 8. Count the number of different sailor names.
SELECT COUNT(DISTINCT sname) AS unique_sailors
FROM Sailors;

-- 9. Find the average age of sailors for each rating level.
SELECT rating, AVG(age) AS avg_age
FROM Sailors
GROUP BY rating;

-- 10. Find the average age of sailors for each rating level that has at least two sailors.
SELECT rating, AVG(age) AS avg_age
FROM Sailors
GROUP BY rating
HAVING COUNT(*) >= 2;
