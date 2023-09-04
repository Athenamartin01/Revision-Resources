SELECT Email,City
FROM Employee;
-- This is a comment
/*
 *Allows us to block comment
*/
SELECT * --Allows us to select all fields from a database
FROM Genre
ORDER BY Genreld ASC --Orders the list by Genreld (int by low to high)((ASC not needed))
ORDER BY Genreld DESC --Orders the list by Genreld (int by high to low)
LIMIT 10 --Takes a maximum of 10 Records
LIMIT 5 OFFSET 2; --Ignores the first 2 records, taking the next 5 

SELECT EmployeeId + 100 AS TOTAL --Creates a new field called total with it's values being 100 + the records's ID value
FROM Employee;

/* + : Addition
*  * : Multiplication
*  
*/

SELECT CONCAT(FirstName, LastName) AS FullName --CONCAT adds 2 strings together
FROM Employee
WHERE FirstName = 'Andrew'; --WHERE allows us to filter the records

/*
 * = Equal to
 * < Less than
 * > Greater than
 * <= Less than or equal
 * >= Greater than or equal
 * <> Not equal
*/

SELECT CONCAT(FirstName, LastName) AS FullName 
FROM Employee
WHERE FirstName LIKE 'And%'; --LIKE looks for similar values, the % alows for matches if the string is present with characters afterwards 

/*Special Characters
 * % fills for any number of characters
 * _ fills for one character
 *
 * 
 * */

SELECT LOWER(FirstName) --LOWER converts to lowercase, UPPER for uppercase
FROM Employee;

MAX(EmployeeId) --Takes the maximum value from the employeeId field
MIN(EmployeeId)
COUNT(EmployeeId) --Counts the number of records from the field
SUM(EmployeeId) --Sums all the values in the field
AVG(EmployeeId) --Takes the average value

-- NULL is used to give blank values
SELECT DISTINCT FirstName --Only takes non duplicate records/fields
FROM Employee
WHERE EmployeeId IS NULL;--Only takes the fields where there is no EId Value (IS NOT NULL) does the opposite

INT -- whole number
FLOAT -- floating point number
DOUBLE -- A double precision floating-point number.
DATE -- A date in YYYY-MM-DD format.
DATETIME -- A date and time combination in YYYY-MM-DD HH:MM:SS format.
TIMESTAMP -- A timestamp, calculated from midnight, January 1, 1970
TIME -- Stores the time in HH:MM:SS format.
VARCHAR(M) -- Variable-length character string. Max size is specified in parenthesis.
TEXT -- Large amount of text data. 
