"""
Part 3

example_School 데이터베이스를 활용하여 이미지로 전달된 결과물울 츌력할 수 있는 SQL 문을 작성합니다.
"""

QUERY_1 = """SELECT teacher_id, student_id, ROW_NUMBER() OVER(ORDER BY teacher_id, student_id) AS '전체 학생순서'
FROM Student;"""

QUERY_2 = """SELECT teacher_id, student_id,
	   ROW_NUMBER() OVER(PARTITION BY teacher_id ORDER BY teacher_id, student_id) AS '선생님별 학생순서'
FROM Student;"""

QUERY_3 = """SELECT student_id, age AS '중앙값'
FROM Student
ORDER BY age
LIMIT 1
OFFSET (SELECT (count(*)/2) FROM Student);"""
