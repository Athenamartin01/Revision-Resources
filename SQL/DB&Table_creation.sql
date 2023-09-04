CREATE DATABASE Alfie; --creates a databse called Alfie

CREATE TABLE Customers ( -- used to create a new table
  id INT AUTO_INCREMENT,
  firstname VARCHAR(128) NOT NULL, --Forces the record to have a value for this field
 lastname VARCHAR(128),
  salary INT DEFAULT 0, --sets a default value of 0
  city VARCHAR(128),
  PRIMARY KEY(ID), --Used to set a key as a primary key
  FOREIGN KEY (<KEY_NAME>) REFERENCES <TABLE>(<KEY>) --Adds a foreign key from <table> 
);

--constraints:
--NOT NULL - cannot be empty
--UNIQUE - has to be unique from other records
--AUTO INCREMENT - adds the next integer value to a new record
--DEFAULT - allows a default value if left empty

INSERT INTO Customers (id, firstname, lastname, salary, city) --Inserts a new record into a table
VALUES 
(1, 'John', 'Smith', 'New York', 5000), 
(2, 'David', 'Williams', 'Los Angeles', 4200);

SELECT salary,city
FROM Customers
WHERE salary > 4500
UPDATE Customers 
SET salary = 4500; --Updates values in the table

DELETE 
FROM Customers 
WHERE salary = 4500;
