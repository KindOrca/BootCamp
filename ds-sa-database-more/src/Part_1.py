"""
Part 1

Chinook 데이터베이스를 이용하여 각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = "SELECT CustomerId, upper(City || ' ' || Country) AS '새로운 컬럼' FROM customers;"

QUERY_2 = "SELECT LOWER(substring(FirstName, 1,4)||substring(LastName, 1,2)) AS '새로운 컬럼' FROM customers;"

QUERY_3 = "SELECT EmployeeId FROM employees AS e WHERE e.HireDate > 2013-01-01 ORDER BY LastName;"

QUERY_4 = """SELECT (FirstName || LastName || InvoiceId) AS new_Invoices
FROM (SELECT *
	  FROM invoices AS i
	  JOIN customers AS c
	  ON c.CustomerId = i.CustomerId
	  ORDER BY c.FirstName, c.LastName, i.InvoiceId);"""

QUERY_5 = """SELECT Name
FROM (SELECT Name
	  FROM tracks AS t
	  LEFT JOIN albums AS a
	  ON t.AlbumId = a.AlbumId
	  WHERE a.Title IN ('Unplugged','Outbreak'));"""
