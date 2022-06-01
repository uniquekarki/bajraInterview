import sqlite3
from prettytable import from_db_cursor

def printTable(cur, table):
    stringQuery = 'SELECT * FROM ' + table
    cur.execute(stringQuery)
    mytable = from_db_cursor(cur)
    print(f'\n{table} Table')
    print(mytable)

def question1(cur):
    queryS = 'SELECT Employee.DeptID, Department.DeptName, round((julianday("now") - julianday(JoinDate)) / 30)*MonthlySalary as TotalEarnings FROM Employee INNER JOIN Department ON Employee.DeptID = Department.DeptID GROUP BY Employee.DeptID'
    cur.execute(queryS)
    resultString = from_db_cursor(cur)
    return resultString

def question2(cur):
    queryS = 'SELECT * FROM Employee WHERE round((julianday("now") - julianday(JoinDate)) / 30) > 6 AND DeptID = 2'
    cur.execute(queryS)
    resultString = from_db_cursor(cur)
    return resultString

def question3(cur):
    # queryS = '''
    #             SELECT 
    #                 *,
    #                 Employee.FirstName,
    #                 Employee.MiddleName,
    #                 Employee.LastName
    #             FROM
    #             (SELECT Employee.EmployeeID, 
    #                     Employee.FirstName, 
    #                     Employee.MiddleName, 
    #                     Employee.LastName, 
    #                     Department.DeptName, 
    #                     Department.ManagerID
    #             FROM Employee 
    #             INNER JOIN Department 
    #             ON Employee.DeptID = Department.DeptID) AS t1
    #             WHERE t1.ManagerID = Employee.EmployeeID
    #             INNER JOIN Employee
    #             ON Employee.EmployeeID = t1.ManagerID'''
    queryS = '''
WITH t1 AS (
  SELECT
    e.EmployeeID,
    e.FirstName,
    e.MiddleName,
    e.LastName,
    d.DeptName,
    d.ManagerID
  FROM Employee e 
  INNER JOIN Department d 
  ON e.deptID = d.DeptID
)

SELECT
  t1.EmployeeID, t1.FirstName, t1.MiddleName, t1.LastName, t1.DeptName,
  CASE WHEN e.MiddleName IS NULL THEN e.FirstName || ' ' || e.LastName 
        ELSE e.FirstName || ' ' || e.MiddleName || ' ' || e.LastName END AS managerName
FROM t1
LEFT JOIN Employee e
ON t1.ManagerID = e.EmployeeID;
    '''
    cur.execute(queryS)
    resultString = from_db_cursor(cur)
    return resultString
# e.FirstName || ' ' || e.LastName AS managerName
if __name__ == '__main__':
    con = sqlite3.connect('task-1-database/bajra.db')
    cur = con.cursor()

    printTable(cur, 'Employee')
    printTable(cur, 'Department')
    
    resultString1 = question1(cur)
    print('\nQUESTION 1:')
    print(resultString1)

    resultString2 = question2(cur)
    print('\nQUESTION 2:')
    print(resultString2)

    resultString3 = question3(cur)
    print('\nQUESTION 3:')
    print(resultString3)