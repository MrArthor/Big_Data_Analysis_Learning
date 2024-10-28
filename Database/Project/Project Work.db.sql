CREATE DATABASE IF NOT EXISTS CustomerFeedbackDB;
USE CustomerFeedbackDB;

DROP TABLE IF EXISTS Feedback_Types;
DROP TABLE IF EXISTS Feedback;
DROP TABLE IF EXISTS Customers;

-- Create Feedback_Types table
CREATE TABLE Feedback_Types (
    Feedback_Type_ID INT AUTO_INCREMENT PRIMARY KEY,
    Type_Name VARCHAR(255) NOT NULL UNIQUE
);

-- Create Customers table
CREATE TABLE Customers (
    Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(100) NOT NULL,
    Last_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Phone_Number VARCHAR(15),
    Registration_Date DATE NOT NULL,
    CONSTRAINT chk_email CHECK (Email LIKE '%@%')
);

-- Create Feedback table
CREATE TABLE Feedback (
    Feedback_ID INT AUTO_INCREMENT PRIMARY KEY,
    Customer_ID INT,
    Feedback_Type_ID INT,
    Feedback_Text TEXT NOT NULL,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Feedback_Date DATE NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
    FOREIGN KEY (Feedback_Type_ID) REFERENCES Feedback_Types(Feedback_Type_ID)
);

-- Insert data into Feedback_Types
INSERT INTO Feedback_Types (Type_Name) VALUES 
('Product Review'),
('Customer Service Experience'),
('Suggestion'),
('Complaint'),
('Query');

-- Insert data into Customers
INSERT INTO Customers (First_Name, Last_Name, Email, Phone_Number, Registration_Date) VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2024-01-15'),
('Jane', 'Smith', 'jane.smith@example.com', '123-456-7891', '2024-01-16'),
('Emily', 'Johnson', 'emily.johnson@example.com', '123-456-7892', '2024-01-17'),
('Michael', 'Brown', 'michael.brown@example.com', '123-456-7893', '2024-01-18'),
('Sarah', 'Davis', 'sarah.davis@example.com', '123-456-7894', '2024-01-19'),
('David', 'Wilson', 'david.wilson@example.com', '123-456-7895', '2024-01-20'),
('Laura', 'Miller', 'laura.miller@example.com', '123-456-7896', '2024-01-21'),
('Daniel', 'Taylor', 'daniel.taylor@example.com', '123-456-7897', '2024-01-22'),
('Olivia', 'Moore', 'olivia.moore@example.com', '123-456-7898', '2024-01-23'),
('James', 'Anderson', 'james.anderson@example.com', '123-456-7899', '2024-01-24'),
('Sophia', 'Thomas', 'sophia.thomas@example.com', '123-456-7800', '2024-01-25'),
('Jacob', 'Jackson', 'jacob.jackson@example.com', '123-456-7801', '2024-01-26'),
('Mia', 'White', 'mia.white@example.com', '123-456-7802', '2024-01-27'),
('Ethan', 'Harris', 'ethan.harris@example.com', '123-456-7803', '2024-01-28'),
('Ava', 'Martin', 'ava.martin@example.com', '123-456-7804', '2024-01-29'),
('William', 'Garcia', 'william.garcia@example.com', '123-456-7805', '2024-01-30'),
('Isabella', 'Martinez', 'isabella.martinez@example.com', '123-456-7806', '2024-01-31'),
('Benjamin', 'Roberts', 'benjamin.roberts@example.com', '123-456-7807', '2024-02-01'),
('Charlotte', 'Clark', 'charlotte.clark@example.com', '123-456-7808', '2024-02-02'),
('Alexander', 'Rodriguez', 'alexander.rodriguez@example.com', '123-456-7809', '2024-02-03'),
('Amelia', 'Lewis', 'amelia.lewis@example.com', '123-456-7810', '2024-02-04');

-- Insert data into Feedback
INSERT INTO Feedback (Customer_ID, Feedback_Type_ID, Feedback_Text, Rating, Feedback_Date) VALUES 
(1, 1, 'Great product, will buy again!', 5, '2024-09-01'),
(2, 2, 'Customer service was very helpful.', 4, '2024-09-02'),
(3, 3, 'I would like to see more options available.', 3, '2024-09-03'),
(4, 4, 'Had an issue with my order, very disappointed.', 2, '2024-09-04'),
(5, 5, 'How do I track my order?', 4, '2024-09-05'),
(6, 1, 'The product quality was below expectations.', 2, '2024-09-06'),
(7, 2, 'Customer support resolved my issue quickly.', 5, '2024-09-07'),
(8, 3, 'Suggestion for better packaging.', 3, '2024-09-08'),
(9, 4, 'Received a defective item, need a replacement.', 1, '2024-09-09'),
(10, 5, 'Where can I find the user manual?', 4, '2024-09-10'),
(11, 1, 'Satisfactory purchase, could be improved.', 3, '2024-09-11'),
(12, 2, 'Friendly and knowledgeable staff.', 5, '2024-09-12'),
(13, 3, 'Add more colors to the product line.', 4, '2024-09-13'),
(14, 4, 'Terrible experience, will not return.', 1, '2024-09-14'),
(15, 5, 'Need more information on return policies.', 4, '2024-09-15'),
(16, 1, 'Overall good, but delivery was late.', 3, '2024-09-16'),
(17, 2, 'Excellent service, keep it up!', 5, '2024-09-17'),
(18, 3, 'Would love to see a loyalty program.', 4, '2024-09-18'),
(19, 4, 'Very poor quality, very dissatisfied.', 1, '2024-09-19'),
(20, 5, 'How to update account information?', 4, '2024-09-20');


SELECT * FROM Customers;

SELECT * FROM Feedback_Types;

SELECT * FROM Feedback WHERE Customer_ID = 1;

SELECT * FROM Feedback WHERE Feedback_Type_ID = 1;

SELECT COUNT(*) AS Total_Feedback FROM Feedback;

SELECT c.First_Name, c.Last_Name, f.Feedback_Text, f.Rating, f.Feedback_Date
FROM Customers c
JOIN Feedback f ON c.Customer_ID = f.Customer_ID;


SELECT ft.Type_Name, AVG(f.Rating) AS Average_Rating
FROM Feedback f
JOIN Feedback_Types ft ON f.Feedback_Type_ID = ft.Feedback_Type_ID
GROUP BY ft.Type_Name;

SELECT c.Customer_ID, c.First_Name, c.Last_Name, f.Feedback_Text, f.Feedback_Date
FROM Customers c
JOIN Feedback f ON c.Customer_ID = f.Customer_ID
WHERE f.Feedback_Date = (
    SELECT MAX(Feedback_Date)
    FROM Feedback f2
    WHERE f2.Customer_ID = c.Customer_ID
);

SELECT c.Customer_ID, c.First_Name, c.Last_Name, COUNT(f.Feedback_ID) AS Feedback_Count
FROM Customers c
JOIN Feedback f ON c.Customer_ID = f.Customer_ID
GROUP BY c.Customer_ID
HAVING COUNT(f.Feedback_ID) > 1;

SELECT f.Feedback_Text, f.Rating
FROM Feedback f
JOIN Feedback_Types ft ON f.Feedback_Type_ID = ft.Feedback_Type_ID
WHERE ft.Type_Name = 'Product Review' AND f.Rating > 3;

