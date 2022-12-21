"""
Part 2

Chinook.db를 이용하여 각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다. 데이터베이스 엔진은 SQLite를 사용합니다.
"""

QUERY_1 = """SELECT Title FROM albums WHERE AlbumId = 31;"""

QUERY_2 = """SELECT AlbumId
FROM albums AS a1
JOIN artists a2 ON a1.ArtistId = a2.ArtistId
WHERE a2.Name LIKE '%the%';"""

QUERY_3 = """SELECT InvoiceId
FROM invoices AS i
WHERE i.BillingCity IN ('Stuttgart', 'Oslo', 'Redmond')
ORDER BY i.InvoiceId;"""

QUERY_4 = """SELECT TrackId
FROM tracks AS t
WHERE t.Name Like 'The%';"""

QUERY_5 = """SELECT CustomerId
FROM customers AS c
WHERE c.Email LIKE '%gmail.com';"""

QUERY_6 = """SELECT InvoiceId
FROM invoices AS i
WHERE i.CustomerId IN (29,30,63)
AND i.Total BETWEEN 1 and 3;"""

QUERY_7 = """SELECT TrackId
FROM tracks AS t
WHERE t.GenreId = (SELECT g.GenreId
				   FROM genres AS g 
				   WHERE g.Name = 'Soundtrack')
AND t.Milliseconds BETWEEN 300000 AND 400000;"""

QUERY_8 = """SELECT COUNT(*) as The_Num_of_customers_X_Country
FROM customers AS c
GROUP BY c.Country;"""

QUERY_9 = """SELECT CustomerId
FROM ((SELECT CustomerId, sum(Total)
	  FROM invoices AS i
	  GROUP BY CustomerId
	  ORDER BY sum(Total) DESC))
LIMIT 5;"""

QUERY_10 = """SELECT Name AS genre_name, count(DISTINCT CustomerId) AS The_Number_of_Customer_ID
FROM invoice_items AS ii
LEFT JOIN invoices i
	ON ii.InvoiceId = i.InvoiceId
LEFT JOIN (SELECT T.TrackId, g.Name 
		   FROM tracks AS t
		   JOIN genres AS g
		   ON t.GenreId = g.GenreId) AS TT
	ON II.trackId = TT.trackId
GROUP BY Name;"""
