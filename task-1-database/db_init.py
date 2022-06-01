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
                    FOREIGN KEY (DeptID) REFERENCES Department (DeptID) 
               )''')

cur.execute('''CREATE TABLE Department
               (
                    DeptID int NOT NULL PRIMARY KEY,
                    DeptName varchar(255) NOT NULL,
                    DeptCode varchar(255),
                    ParentDeptID int NOT NULL,
                    ManagerID int,
                    Description text,
                    Active BIT NOT NULL,
                    FOREIGN KEY (ManagerID) REFERENCES Employee (EmployeeID)
               )''')

cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (1, 'Ram', None, 'Wagle', datetime.date(2015, 3, 1), 50000, 1))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (2, 'Shyam', 'Prashad', 'Dahal', datetime.date(2016, 4, 2), 50000, 1))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (3, 'Hari', None, 'KC', datetime.date(2015, 5, 3), 50000, 1))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (4, 'Bikram', 'Bahadur', 'Shrestha', datetime.date(2021, 6, 3), 60000, 2))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (5, 'Mohit', None, 'Shakya', datetime.date(2020, 6, 4), 60000, 2))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (6, 'Laxman', None, 'Rai', datetime.date(2021, 7, 5), 60000, 2))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (7, 'Sita', None, 'Chaudary', datetime.date(2015, 8, 6), 70000, 3))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (8, 'Babin', None, 'Joshi', datetime.date(2013, 3, 1), 150000, 2)) #Manager
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (9, 'Utsav', None, 'Darlami', datetime.date(2013, 4, 2), 150000, 4))#Manager
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (10, 'Gyanas', None, 'Luitel', datetime.date(2015, 5, 3), 70000, 3)) 
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (11, 'Asim', 'Singh', 'Mahat', datetime.date(2013, 6, 3), 150000, 3))#Manager
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (12, 'Bhabuk', None, 'Kunwar', datetime.date(2013, 6, 4), 150000, 1))#Manager
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (13, 'Gyanas', None, 'Luitel', datetime.date(2015, 5, 3), 70000, 3))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (14, 'Arun', 'Kumar', 'Regmi', datetime.date(2021, 6, 3), 80000, 4))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (15, 'Pratap', None, 'Malla', datetime.date(2020, 6, 4), 80000, 4))
cur.execute("INSERT INTO Employee VALUES (?,?,?,?,?,?,?)", (16, 'Ashok', None, 'Shah', datetime.date(2020, 6, 4), 80000, 4))

cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (1, 'Frontend', 'i', 9, 12, 'Frontend developer specilizing in React framework',1))
cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (2, 'Sales', 'ii', 8, 8, 'Sales department',1))
cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (3, 'HR', 'iii', 7, 11, 'Human Resource department',1))
cur.execute("INSERT INTO Department VALUES (?,?,?,?,?,?,?)", (4, 'Python', 'iv', 6, 9, 'Python developer',1))

# Save (commit) the changes
con.commit()

print('Database Sucessfully Created!')

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()