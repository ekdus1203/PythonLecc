import cx_Oracle
import os
import sys

os.environ['NLS_LANG'] = '.AL32UTF8'
dsn = cx_Oracle.makedsn("127.0.0.1", 1521, "xe")

# 1) 연결 객채 생성
conn = cx_Oracle.connect("bitPython","bitPython",dsn)
# 2) 커서 객체 생성
cursor = conn.cursor()
# 3) student 테이블에 데이터 삽입

cursor.execute("""INSERT INTO student (id, name, age, addr)
     VALUES(student_id_seq.nextval,'홍길동', '24','지리산')""")
conn.commit()

# 4) student 테이블 데이터 가져오기
cursor.execute("SELECT * FROM student")
for row in cursor:
    print(row)

cursor.close()
conn.close()