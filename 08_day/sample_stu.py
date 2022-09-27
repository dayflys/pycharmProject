from pprint import pprint

import cx_Oracle

con = None
def db_init():
    user = "workshop"
    pw = "workshop"
    dsn = "localhost/xe"
    global con
    con = cx_Oracle.connect(user, pw, dsn, encoding="UTF-8")

def init():

    while(True):
        main_print()
        menu = input("메뉴입력 =>")
        if menu == '1':
            student_all_list()
        elif menu == '2':
            student_choose_list()
        elif menu == '3':
            entrance_date_list()
        elif menu == '4':
            student_no_many_list()
        elif menu == '5':
            absence_change_many()
        elif menu == '6':
            capacity_change_many()
        elif menu == '7':
            point_list()
        elif menu == '8':
            cur_commit()
        elif menu == '9':
            rollback()
        else:
            print("프로그램이 종료되었습니다.")
            exit()

def main_print():
    print("*" * 30)
    print("1. 전체 학생 목록")
    print("2. 학생 이름 검색")
    print("3. 학생 입학년도 범위 검색 (예> 2000부터 2003년까지)")
    print("4. 학생 학번으로 다중 검색(쉼표 구분자) ")
    print("5. 학생 휴학 일괄 수정(쉼표 구분자) ")
    print("6. 학과 정원 일괄 수정 ")
    print("7. 학생 학점 검색 ")
    print("8. commit ")
    print("9. rollback ")
    print("0. 종료")

def student_all_list():
    with con.cursor() as cur:
        cur.execute("select student_no ,student_name ,student_ssn ,student_address , entrance_date, absence_yn from tb_student order by student_no")
        result = cur.fetchall()
        print('='*100)
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        print('-'*100)
        for no, name, ssn, add,date,yn in result:
            ssn = ssn[:8] +'*'*6
            if add is None:
                add = "***주소미상***"
            else:
                add = add[:10]+"..."
            date = date.strftime('%Y/%M/%d')
            yn = yn.upper()
            print(no,'\t',name,'\t',ssn,'\t',add,'\t',date,'\t',yn)

        print()
        print('총 학생 수: ', cur.rowcount)

def student_choose_list():
    name= input("검색할 학생명을 입력하시오")
    name = name.strip()
    with con.cursor() as cur:
        cur.execute(f"select student_no ,student_name ,student_ssn ,student_address , entrance_date, absence_yn from tb_student where student_name like '%{name}%' order by student_no")
        result = cur.fetchall()
        print('='*100)
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        print('-'*100)
        for no, name, ssn, add,date,yn in result:
            ssn = ssn[:8] +'*'*6
            if add is None:
                add = "***주소미상***"
            else:
                add = add[:10]+"..."
            date = date.strftime('%Y/%M/%d')
            yn = yn.upper()
            print(no,'\t',name,'\t',ssn,'\t',add,'\t',date,'\t',yn)

        print()
        print('총 학생 수: ', cur.rowcount)

def entrance_date_list():
    start = input("시작 입학년도를 입력하시요")
    end = input("끝 입학년도를 입력하시오")
    with con.cursor() as cur:
        cur.execute(f"select student_no ,student_name ,student_ssn ,student_address , entrance_date, absence_yn from tb_student where entrance_date between to_date('{start}/03/01','YYYY/MM/DD') and to_date('{end}/03/01','YYYY/MM/DD') order by student_no")
        result = cur.fetchall()
        print('='*100)
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        print('-'*100)
        for no, name, ssn, add,date,yn in result:
            ssn = ssn[:8] +'*'*6
            if add is None:
                add = "***주소미상***"
            else:
                add = add[:10]+"..."
            date = date.strftime('%Y/%M/%d')
            yn = yn.upper()
            print(no,'\t',name,'\t',ssn,'\t',add,'\t',date,'\t',yn)

        print()
        print('총 학생 수: ', cur.rowcount)

def student_no_many_list():
    number = input("검색할 학생의 학번을 입력하시요")
    student_no = number.split(',')
    student_list = []
    with con.cursor() as cur:
        for i in student_no:
            cur.execute(f"select student_no ,student_name ,student_ssn ,student_address , entrance_date, absence_yn from tb_student where student_no = '{i}' order by student_no")
            result = cur.fetchall()
            student_list.append(result)
        print('='*100)
        print("학번\t\t\t이름\t\t\t\t주민번호\t\t\t\t주소\t\t\t\t\t\t\t\t입학년도\t\t\t\t휴학여부")
        print('-'*100)
        for num in student_list:
            for no, name, ssn, add,date,yn in num:
                ssn = ssn[:8] +'*'*6
                if add is None:
                    add = "***주소미상***"
                else:
                    add = add[:10]+"..."
                date = date.strftime('%Y/%M/%d')
                yn = yn.upper()
                print(no,'\t',name,'\t',ssn,'\t',add,'\t',date,'\t',yn)

        print()
        print('총 학생 수: ', cur.rowcount)

def absence_change_many():
    number = input("수정할 학생의 학번을 입력하시요")
    student_no = number.split(',')
    with con.cursor() as cur:
        for i in student_no:
            cur.execute(f"update tb_student set absence_yn = 'Y' where student_no = '{i}'")
        con.commit()
        print()
        print('총 변경학생 수: ', cur.rowcount)

def capacity_change_many():
    with con.cursor() as cur:
        cur.execute("update tb_department set capacity = case when capacity <= 20 then capacity+5 when capacity <= 25 then capacity+4 when capacity <= 30 then capacity+3 else capacity end")
        con.commit()
        print()
        print('총 변경학생 수: ', cur.rowcount)


def point_list():
    number = input("학생의 학번을 입력하시요")
    with con.cursor() as cur:
        cur.execute(f"select term_no,tb_grade.student_no ,student_name,class_name ,point from tb_student,tb_grade,tb_class where tb_student.student_no = tb_grade.student_no and tb_student.student_no ='{number}' and tb_grade.class_no = tb_class.class_no order by student_no")
        result = cur.fetchall()
        print('=' * 100)
        print("학기\t\t학번\t\t\t이름\t\t과목명\t\t\t\t점수\t\t학점")
        print('-' * 100)
        for term, num, name, cname, point in result:
            if point < 2:
                grade = "F학점"
            elif point < 3:
                grade = "D학점"
            elif point < 3.5:
                grade = "C학점"
            elif point < 4:
                grade = "B학점"
            else:
                grade = "A학점"
            print(term, '\t', num, '\t', name, '\t', cname, '\t', point, '\t', grade)

def cur_commit():
    with con.cursor() as cur:
        con.commit()
        print('커밋 되었습니다')

def rollback():
    with con.cursor() as cur:
        con.rollback()
        print('롤백 되었습니다')


if __name__ == '__main__':
    db_init()
    init()