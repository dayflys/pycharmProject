'''

    dept 테이블 관리
    1. 전체 조회
    2. 특정 부서 조회
    3. 부서 저장
    4. 부서 수정
    5. 부서 삭제
'''
from pprint import pprint

#DB 연동 초기화
import cx_Oracle

def DB_init():
    user ="SCOTT"
    pw = "TIGER"
    dns = "localhost:1521/xe"
    global con
    con = cx_Oracle.connect(user,pw,dns, encoding='utf-8')


def init():
    while True:
        if not input(): print()
        menu_print()
        menu = input("메뉴 입력")
        try:
            if menu == "1":
                dept_all_list()
            elif menu == '2':
                find_by_deptno()
            elif menu == '3':
                dept_insert()
            elif menu == '4':
                dept_update()
            elif menu == '5':
                dept_delete()
            elif menu == '0':
                con.close()
                exit()
            else:
                continue
        except Exception as e:
            print('다시 해주세요')
            print()
            print(e)
#전체 조회
def dept_all_list():
    with con.cursor() as cur:
        cur.execute("select deptno, dname, loc from dept ")
        result = cur.fetchall()
        pprint(result)
        print()
        print('총 레코드 개수: ', cur.rowcount)

#특정 부서 조회
def find_by_deptno():
    deptno = input('검색할 부서번호를 입력하시오')
    with con.cursor() as cur:
        cur.execute("select deptno, dname, loc from dept where deptno = :XXX", XXX=deptno)
        result = cur.fetchone()
        if not result:
            raise Exception
        pprint(result)
        print()

#부서 저장
def dept_insert():
    deptno = input('저장할 부서번호를 입력하시오')
    dname = input('저장할 부서명를 입력하시오')
    loc = input('저장할 위치를 입력하시오')
    with con.cursor() as cur:  # : => 바인딩 변수
        cur.execute("insert into dept (deptno, dname, loc) values ( :deptno, :dname, :loc )", deptno=deptno, dname=dname,
                    loc=loc)
        cur.execute("select deptno, dname, loc from dept where deptno = :XXX", XXX=deptno)
        result = cur.fetchone()
        print(result)
        print()
        print("저장된 레코드 개수: ", cur.rowcount)
        con.commit()

#부서 수정
def dept_update():
    deptno = input('수정할 부서번호를 입력하시오')
    dname = input('수정할 부서명를 입력하시오')
    loc = input('수정할 위치를 입력하시오')
    with con.cursor() as cur:
        cur.execute("update dept set dname =:dname, loc=:loc where deptno =: deptno", dname=dname, loc=loc, deptno=deptno)
        cur.execute("select deptno, dname, loc from dept where deptno = :XXX", XXX=deptno)
        result = cur.fetchone()
        print(result)
        print()
        print("수정된 레코드 갯수:", cur.rowcount)
        con.commit()

#부서 삭제
def dept_delete():
    deptno = input("삭제할 부서번호를 입력해주세요")
    with con.cursor() as cur:
        cur.execute("delete from dept where deptno =: deptno", deptno=deptno)
        print()
        if not cur.rowcount:
            raise Exception
        else:
            print("삭제된 레코드 갯수:", cur.rowcount)
        con.commit()

#메뉴 출력
def menu_print():
    print("*" * 100)
    print("1. 전체 부서 목록 ")
    print("2. 특정 부서 조회 ")
    print("3. 부서 저장 ")
    print("4. 부서 수정 ")
    print("5. 부서 삭제")
    print("0. 종료")
    print("*" * 100)

#시작점 역할
if __name__ == "__main__":
    DB_init()
    init()