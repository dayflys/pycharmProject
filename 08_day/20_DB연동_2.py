'''
    파이썬 연동

'''
import cx_Oracle

user = "SCOTT"
pw ="TIGER"
dns ='localhost:1521/xe'

con = cx_Oracle.connect(user,pw, dns, encoding='utf-8')
print(con) #<cx_Oracle.Connection to SCOTT@localhost:1521/xe>

#1. insert - 단일행 저장 => execute
with con.cursor() as cur:# : => 바인딩 변수
    cur.execute("insert into dept (deptno, dname, loc) values ( :deptno, :dname, :loc )", deptno = 97, dname='관리', loc= '서울')
    print("저장된 레코드 개수: ", cur.rowcount)
    con.commit()


#2. insert- 다중행 저장 => executemany
rows = [(67, 'ACCOUNTING', 'NEW YORK'), (72, '개발', '서울')]
with con.cursor() as cur:# : => 바인딩 변수
    cur.executemany("insert into dept (deptno, dname, loc) values ( :1, :2, :3 )", rows)
    print("저장된 레코드 개수: ", cur.rowcount)
    con.commit()
con.close()