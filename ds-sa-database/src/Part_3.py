"""
Part 3

STORE.db를 이용하여 각 이미지로 전달된 결과가 출력될 수 있는 SQL 문을 작성합니다. 데이터베이스 엔진은 SQLite를 사용합니다.
"""

QUERY_1 = """SELECT c.id, c.name, i.invoice_amt
FROM Customers AS c
LEFT JOIN Invoices AS i
	ON c.id = i.customer_id
LIMIT 2
OFFSET 10;"""

QUERY_2 = """SELECT i.customer_id, c.name, i.invoice_amt
FROM Invoices AS i
LEFT JOIN Customers AS c
	ON c.id = i.customer_id
LIMIT 2
OFFSET 10;"""

QUERY_3 = """SELECT id, customer_id, date(invoice_date) AS '날짜', invoice_amt
FROM Invoices AS i
ORDER BY invoice_amt DESC;"""

