CREATE DATABASE LargeDatasetDB;
USE LargeDatasetDB;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15),
    DateOfBirth DATE,
    City VARCHAR(50),
    Country VARCHAR(50),
    SignupDate DATE
);


CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10, 2),
    StockQuantity INT
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, DateOfBirth, City, Country, SignupDate)
VALUES
('John', 'Doe', 'john.doe@email.com', '1234567890', '1985-02-15', 'New York', 'USA', '2022-05-01'),
('Jane', 'Smith', 'jane.smith@email.com', '2345678901', '1990-06-10', 'Los Angeles', 'USA', '2022-07-15'),
('Mike', 'Brown', 'mike.brown@email.com', '3456789012', '1982-08-22', 'Chicago', 'USA', '2022-08-22'),
('Emily', 'Davis', 'emily.davis@email.com', '4567890123', '1993-12-12', 'Houston', 'USA', '2022-09-03'),
('Chris', 'Wilson', 'chris.wilson@email.com', '5678901234', '1987-04-19', 'Miami', 'USA', '2022-10-05'),
('Alice', 'Johnson', 'alice.johnson@email.com', '6789012345', '1975-05-15', 'Boston', 'USA', '2022-11-02'),
('Bob', 'Williams', 'bob.williams@email.com', '7890123456', '1980-01-20', 'Austin', 'USA', '2022-11-15'),
('David', 'Miller', 'david.miller@email.com', '8901234567', '1972-09-11', 'Dallas', 'USA', '2022-12-05'),
('Sara', 'Wilson', 'sara.wilson@email.com', '9012345678', '1988-03-30', 'Denver', 'USA', '2022-12-20'),
('Tom', 'Harris', 'tom.harris@email.com', '0123456789', '1986-10-18', 'Phoenix', 'USA', '2022-10-29'),
 for testing
('Sam', 'Owen', 'sam.owen@email.com', '1230001234', '1980-11-15', 'London', 'UK', '2022-09-11'),
('Sophie', 'Taylor', 'sophie.taylor@email.com', '1456023433', '1992-05-19', 'Berlin', 'Germany', '2022-07-17'),
('Thomas', 'Green', 'thomas.green@email.com', '6561236784', '1979-07-04', 'Rome', 'Italy', '2022-11-30'),
('Olivia', 'Martin', 'olivia.martin@email.com', '7389995124', '1985-12-09', 'Paris', 'France', '2022-05-11'),
('Noah', 'Lee', 'noah.lee@email.com', '9839876753', '1987-08-14', 'Tokyo', 'Japan', '2022-06-13'),
('Ava', 'Scott', 'ava.scott@email.com', '7291238743', '1991-04-07', 'Sydney', 'Australia', '2022-09-08'),
('Mason', 'Kim', 'mason.kim@email.com', '5236237124', '1994-01-19', 'Seoul', 'South Korea', '2022-09-09'),
('Lucas', 'Harris', 'lucas.harris@email.com', '3412235445', '1990-07-21', 'Singapore', 'Singapore', '2022-10-02');


INSERT INTO Products (ProductName, Category, Price, StockQuantity)
VALUES
('Laptop', 'Electronics', 899.99, 50),
('Smartphone', 'Electronics', 699.99, 100),
('Tablet', 'Electronics', 299.99, 150),
('Headphones', 'Accessories', 79.99, 200),
('Camera', 'Photography', 499.99, 80),
('Gaming Console', 'Electronics', 499.99, 90),
('Smartwatch', 'Wearable', 199.99, 150),
('Wireless Mouse', 'Accessories', 29.99, 300),
('Mechanical Keyboard', 'Accessories', 109.99, 120),
('Monitor', 'Electronics', 249.99, 70),

('External Hard Drive', 'Storage', 119.99, 90),
('Router', 'Networking', 89.99, 100),
('USB Flash Drive', 'Storage', 14.99, 300),
('Bluetooth Speaker', 'Accessories', 49.99, 150),
('Smart TV', 'Electronics', 1099.99, 60),
('Drone', 'Photography', 999.99, 40),
('Digital Camera', 'Photography', 599.99, 80),
('Graphics Card', 'PC Components', 599.99, 50),
('Processor', 'PC Components', 399.99, 80),
('Power Supply', 'PC Components', 129.99, 110);

INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
VALUES
(1, '2023-01-15', 1599.97),
(2, '2023-02-10', 699.99),
(3, '2023-03-05', 1199.98),
(4, '2023-04-08', 879.98),
(5, '2023-05-11', 999.99),
(6, '2023-05-21', 349.99),
(7, '2023-06-03', 549.99),
(8, '2023-07-12', 2099.99),
(9, '2023-08-18', 799.99),
(10, '2023-09-02', 999.99),

(11, '2023-09-05', 649.99),
(12, '2023-10-01', 2999.99),
(13, '2023-10-12', 749.99),
(14, '2023-11-19', 1799.99),
(15, '2023-12-20', 399.99);

INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice)
VALUES
(1, 1, 1, 899.99),
(1, 4, 2, 79.99),
(2, 2, 1, 699.99),
(3, 1, 1, 899.99),
(3, 5, 1, 499.99),
(4, 3, 2, 299.99),
(5, 4, 5, 79.99),
(6, 6, 1, 349.99),
(7, 7, 1, 199.99),
(8, 8, 3, 29.99),

(9, 9, 1, 109.99),
(10, 10, 2, 249.99),
(11, 1, 1, 899.99),
(12, 3, 2, 299.99),
(13, 4, 5, 79.99);


SELECT * FROM Customers;

SELECT FirstName, LastName, City, Country FROM Customers WHERE Country = 'USA';


SELECT O.OrderID, C.FirstName, C.LastName, O.TotalAmount, O.OrderDate
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;


SELECT P.Category, SUM(OI.Quantity * OI.UnitPrice) AS TotalSales
FROM OrderItems OI
JOIN Products P ON OI.ProductID = P.ProductID
GROUP BY P.Category;


SELECT SUM(TotalAmount) AS TotalRevenue FROM Orders;

SELECT AVG(TotalAmount) AS AverageOrderValue FROM Orders;

select version();

SELECT CustomerID, SUM(TotalAmount) AS TotalSpent
FROM Orders
GROUP BY CustomerID
HAVING TotalSpent > 2000;

DELETE FROM Customers WHERE CustomerID = 8;
select * from Customers;


select * from Customers group by country having count(*)>1;

create view view_name as 
select * from Customers;

select * from Customers;

insert into view_name (FirstName, LastName, Email, PhoneNumber, DateOfBirth, City, Country, SignupDate) values ('Jhn', 'Doe', 'doe@email.com', '1234567', '1985-02-15', 'New York', 'USA', '2022-05-01')

