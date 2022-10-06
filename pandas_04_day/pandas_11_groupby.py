'''
    DataFrame의 그룹핑

    df.groupby(by='컬럼명')['sal'].그룹함수
'''
import pandas as pd
import numpy as np

department = {"deptno":[10,20,30,40],'dname':['개발','인사','영업','관리'],'loc':['서울','부산','제주','광주']}
employee = {"empno":['A1','A2','A3','A4','A5'],"ename":['홍길동','유관순','안중근','강감찬','이순신'],
            "sal":[1000,1500,2300,3400,4500],"hireday":['2019/01/02','2018/01/02','2019/01/02','2016/01/02','2015/01/02'],
            "deptno":[10,20,10,30,10]}
d_df = pd.DataFrame(department)
e_df = pd.DataFrame(employee)

print(d_df)
'''
   deptno dname loc
0      10    개발  서울
1      20    인사  부산
2      30    영업  제주
3      40    관리  광주
'''
print(e_df)
'''
  empno ename   sal     hireday  deptno
0    A1   홍길동  1000  2019/01/02      10
1    A2   유관순  1500  2018/01/02      20
2    A3   안중근  2300  2019/01/02      10
3    A4   강감찬  3400  2016/01/02      30
4    A5   이순신  4500  2015/01/02      10
'''
print('1. 부서별 sal 최대값')
new_df = e_df.groupby(by='deptno')['sal'].max()
print(new_df)
'''
1. 부서별 sal 최대값
deptno
10    4500
20    1500
30    3400
Name: sal, dtype: int64
'''
print('1. 부서별 sal 최소값')
new_df = e_df.groupby(by='deptno')['sal'].min()
print(new_df)
'''
1. 부서별 sal 최소값
deptno
10    1000
20    1500
30    3400
Name: sal, dtype: int64
'''
print('1. 부서별 sal 합계')
new_df = e_df.groupby(by='deptno')['sal'].sum()
print(new_df)
'''
1. 부서별 sal 합계
deptno
10    7800
20    1500
30    3400
Name: sal, dtype: int64
'''
print('1. 부서별 sal 평균')
new_df = e_df.groupby(by='deptno')['sal'].mean()
print(new_df)
'''
deptno
10    2600.0
20    1500.0
30    3400.0
Name: sal, dtype: float64
'''
print('1. 부서별 sal 개수')
new_df = e_df.groupby(by='deptno')['sal'].count() #select count(sal)
print(new_df)
'''
1. 부서별 sal 개수
deptno
10    3
20    1
30    1
Name: sal, dtype: int64
'''
print('1. 부서별 전체 레코드 개수')
new_df = e_df.groupby(by='deptno').size() #select count(*)
print(new_df)
'''
deptno
10    3
20    1
30    1
dtype: int64
'''

print('2. 부서별 입사일별 sal 최대값')
new_df = e_df.groupby(by=['deptno','hireday'])["sal"].max()
print(new_df)
'''
2. 부서별 입사일별 sal 최대값
deptno  hireday   
10      2015/01/02    4500
        2019/01/02    2300
20      2018/01/02    1500
30      2016/01/02    3400
'''
