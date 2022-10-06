'''
    DataFrame의 그룹핑

    1.df.groupby(by='컬럼명')['sal'].그룹함수
        -> new_df = e_df.groupby(by='deptno')['sal'].max()

    2.df.groupby(by='컬럼명')['sal'].agg(그룹 함수명|사용자 지정 함수명)
        -> new_df = e_df.groupby(by='deptno')['sal'].agg('np.max')
        -> new_df = e_df.groupby(by='deptno')['sal'].agg('max')
    ==> agg 쓰는 이유 : 그룹함수를 리스트로 여러개 사용 가능하다.

     3. df.groupby(by='컬럼명')['sal'].agg([그룹함수명,그룹함수명2,....])

     4. 컬럼 단위로 그룹함수 적용
        df.groupby(by='컬럼명').agg({컬럼명:그룹함수명, 컬럼명2:그룹함수명2, ....})

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
new_df = e_df.groupby(by='deptno')['sal'].agg(np.max)
print(new_df)
'''
1. 부서별 sal 최대값
deptno
10    4500
20    1500
30    3400
Name: sal, dtype: int64
'''
new_df = e_df.groupby(by='deptno')['sal'].agg('max')
print(new_df)
'''
deptno
10    4500
20    1500
30    3400
Name: sal, dtype: int64
'''
print('2. 부서별 sal 최대값,최소값,합계,평균')
new_df = e_df.groupby(by='deptno')['sal'].agg([np.max,np.min,np.sum,np.mean])
print(new_df)
'''
2. 부서별 sal 최대값,최소값,합계,평균
        amax  amin   sum    mean
deptno                          
10      4500  1000  7800  2600.0
20      1500  1500  1500  1500.0
30      3400  3400  3400  3400.0
'''
new_df = e_df.groupby(by='deptno')['sal'].agg(['max','min','sum','mean'])
print(new_df)
'''
         max   min   sum    mean
deptno                          
10      4500  1000  7800  2600.0
20      1500  1500  1500  1500.0
30      3400  3400  3400  3400.0
'''
print('3. 부서별 sal 최대값,최소값, deptno는 개수')
new_df = e_df.groupby(by='deptno').agg({'sal':['max','min'],'deptno':'count'})
print(new_df)
'''
         max   min  count
deptno                   
10      4500  1000      3
20      1500  1500      1
30      3400  3400      1
'''
