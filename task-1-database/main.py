import sqlite3
from prettytable import from_db_cursor


if __name__ == '__main__':
    con = sqlite3.connect('task-1-database/bajra.db')
    cur = con.cursor()
    queryS = 'SELECT Employee.DeptID, Department.DeptName, round((julianday("now") - julianday(JoinDate)) / 30)*MonthlySalary as TotalEarnings FROM Employee INNER JOIN Department ON Employee.DeptID = Department.DeptID GROUP BY Employee.DeptID'
    cur.execute(queryS)
    string1 = from_db_cursor(cur)
    print(string1)