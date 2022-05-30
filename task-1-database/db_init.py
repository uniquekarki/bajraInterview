import sqlite3
from prettytable import from_db_cursor
import datetime
con = sqlite3.connect('task-1-database/bajra.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE Employee
               (
                    EmployeeID int NOT NULL PRIMARY KEY,
                    FirstName varchar(255) NOT NULL,
                    MiddleName varchar(255),
                    LastName varchar(255) NOT NULL,
                    JoinDate date,
                    MonthlySalary decimal,
                    DeptID int NOT NULL,
                    CONSTRAINT DeptID FOREIGN KEY (DeptID) REFERENCES Department (DeptID) 
               )''')

cur.execute('''CREATE TABLE Department
               (
                    DeptID int NOT NULL PRIMARY KEY,
                    DeptName varchar(255) NOT NULL,
                    DeptCode varchar(255),
                    ParentDeptID int NOT NULL,
                    ManagerID int,
                    Description text,
                    Active BIT NOT NULL
               )''')

cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (1, 'Ram', None, 'Wagle', datetime.date(2015, 3, 1), 50000, 3))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (2, 'Shyam', 'Prashad', 'Dahal', datetime.date(2016, 4, 2), 40000, 1))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (3, 'Hari', None, 'KC', datetime.date(2015, 5, 3), 60000, 2))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (4, 'Bikram', 'Bahadur', 'Shrestha', datetime.date(2021, 6, 3), 60000, 2))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (5, 'Mohit', None, 'Shakya', datetime.date(2020, 6, 4), 50000, 5))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (6, 'Laxman', None, 'Rai', datetime.date(2021, 7, 5), 90000, 4))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (7, 'Sita', None, 'Chaudary', datetime.date(2015, 8, 6), 80000, 4))

cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (1, 'React', 'i', 9, 10, 'Frontend developer specilizing in React framework',1))
cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (2, 'Ruby', 'ii', 8, 11, 'Backend developer specilizing in Ruby on rails',1))
cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (3, 'HR', 'iii', 7, 12, 'Human Resource manager',1))
cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (4, 'Python', 'iv', 6, 13, 'Python developer',1))
cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (5, 'Account', 'v', 5, 14, 'Accountant that deals with money management',1))


cur.execute("SELECT * FROM Department")
mytable2 = from_db_cursor(cur)
print(mytable2)

cur.execute("SELECT * FROM Employee")
mytable1 = from_db_cursor(cur)
print(mytable1)

# Save (commit) the changes
con.commit()

print('Database Sucessfully Created!')

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()