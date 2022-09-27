'''
    파이썬 연동

'''
import cx_Oracle

user = "SCOTT"
pw ="TIGER"
dns ='localhost:1521/xe'

con = cx_Oracle.connect(user,pw, dns, encoding='utf-8')
print(con) #<cx_Oracle.Connection to SCOTT@localhost:1521/xe>

#1. 단일 행 조회
with con.cursor() as cur:
    cur.execute("select deptno, dname, loc from dept where deptno = 10") #; 없어야 한다.
    result = cur.fetchone() #(10, 'ACCOUNTING', 'NEW YORK') -> 제너레이터 성격을 띈다.
    result = cur.fetchone()  # (10, 'ACCOUNTING', 'NEW YORK')
    print(result)

#2. 단일 행 조회 - 동적인 값 조회
deptno = input("찾고싶은 부서명을 입력하세요")
with con.cursor() as cur:
    cur.execute("select deptno, dname, loc from dept where deptno = :XXX",XXX=deptno) #; 없어야 한다.
    result = cur.fetchone() #(10, 'ACCOUNTING', 'NEW YORK') -> 제너레이터 성격을 띈다.
    print(result)

#3. 다중 행 조회 -
with con.cursor() as cur:
    cur.execute("select deptno, dname, loc from dept where deptno =: xxx or dname =: yyy", xxx= 10 ,yyy="개발") #; 없어야 한다.
    result = cur.fetchall() #[(10, 'ACCOUNTING', 'NEW YORK'), (20, 'RESEARCH', 'DALLAS'), (30, 'SALES', 'CHICAGO'), (40, 'OPERATIONS', 'BOSTON'), (50, '개발', '서울')]
    # for deptno, dname, loc in result:
    #     print('부서번호:{}, 부서명:{}, 위치:{}'.format(deptno,dname,loc))
    print(result)
    print('총 레코드 개수: ', cur.rowcount)

con.close()

