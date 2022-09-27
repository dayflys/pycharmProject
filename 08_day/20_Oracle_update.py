import cx_Oracle

user = "SCOTT"
pw ="TIGER"
dns ='localhost:1521/xe'

con = cx_Oracle.connect(user,pw, dns, encoding='utf-8')
print(con) #<cx_Oracle.Connection to SCOTT@localhost:1521/xe>

#1. update - 단일행 저장 => execute
with con.cursor() as cur:
    cur.execute("update dept set dname =:dname, loc=:loc where deptno =: deptno", dname = "인사", loc="경기", deptno=98)
    print("수정된 레코드 갯수:", cur.rowcount )
    con.commit()

con.close()