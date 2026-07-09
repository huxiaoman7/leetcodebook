SELECT
    d.Name AS Department,
    e.Name AS Employee,
    e.Salary
FROM Employee e
JOIN Department d
    ON e.DepartmentId = d.Id
JOIN (
    SELECT DepartmentId, MAX(Salary) AS Salary
    FROM Employee
    GROUP BY DepartmentId
) m
    ON e.DepartmentId = m.DepartmentId
   AND e.Salary = m.Salary;
