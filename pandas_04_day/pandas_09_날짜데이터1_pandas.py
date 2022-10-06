'''

    pandas 날짜 데이터 처리

    1. 문자열 ===> 날짜로 변경
    pd.to_datetime('문자열', format='')

    2. 지정된 범위만큼 날짜를 생성
    pd.data_range('시작날짜','종료날짜')

    3. 날짜 정보 얻기
    Series.dt.속성
    예> Series.dt.year
        Series.dt.month
        Series.dt.day

    4. 날짜를 문자로 변환
     날짜데이터.astype(str)

'''
import pandas as pd

print('1.날짜로 변경')
print(pd.to_datetime('2022/10/6')) #2022-10-06 00:00:00
print(pd.to_datetime('2022-10-6')) #2022-10-06 00:00:00


# print(pd.to_datetime('2022년10월6일')) #to_datetime함수가 년,월,일을 인식하지 못하므로 에러가 발생한다. 따라서 이런경우에는 포멧을 지정해주면된다.
print(pd.to_datetime('2022년10월6일', format='%Y년%m월%d일')) #2022-10-06 00:00:00
print(pd.to_datetime('20220506173439', format='%Y%m%d%H%M%S')) #2022-05-06 17:34:39

print('2.지정된 범위만큼 날짜를 생성') #기본은 일단위 이다.
xx = pd.date_range('2022-10-6','2022-10-10')
print(xx)
'''
DatetimeIndex(['2022-10-06', '2022-10-07', '2022-10-08', '2022-10-09',
               '2022-10-10'],
              dtype='datetime64[ns]', freq='D')
'''
xx = pd.date_range('2022-10-6','2022-10-10',periods=5) #periods 는 갯수
print(xx)
'''
DatetimeIndex(['2022-10-06', '2022-10-07', '2022-10-08', '2022-10-09',
               '2022-10-10'],
              dtype='datetime64[ns]', freq=None)
'''
xx = pd.date_range('2022-10-6', periods=5, freq="D") #freq는 단위를 나타낸닦
print(xx)
'''
DatetimeIndex(['2022-10-06', '2022-10-07', '2022-10-08', '2022-10-09',
               '2022-10-10'],
              dtype='datetime64[ns]', freq='D')
'''
xx = pd.date_range('2022-10-6', periods=5, freq="M")
print(xx)
'''
DatetimeIndex(['2022-10-31', '2022-11-30', '2022-12-31', '2023-01-31',
               '2023-02-28'],
              dtype='datetime64[ns]', freq='M')
'''
xx = pd.date_range('2022-10-6', periods=5, freq="Y")
print(xx)
'''
DatetimeIndex(['2022-12-31', '2023-12-31', '2024-12-31', '2025-12-31',
               '2026-12-31'],
              dtype='datetime64[ns]', freq='A-DEC')'''

#응용 ===> 날짜를 인덱스 라벨로 지정
xx = pd.date_range('2022-10-6', periods=5, freq="M")
df = pd.DataFrame({'price': range(5)}, index=xx)
print(df)
'''
            price
2022-10-31      0
2022-11-30      1
2022-12-31      2
2023-01-31      3
2023-02-28      4
'''
xx = pd.date_range('2022-10-6', periods=5, freq="M")
df = pd.DataFrame({'date':xx,'price': range(5)})
print(df)
'''
        date  price
0 2022-10-31      0
1 2022-11-30      1
2 2022-12-31      2
3 2023-01-31      3
4 2023-02-28      4
'''
print('3. 날짜 정보 얻기')
print("년도")
print(df['date'].dt.year)
'''
년도
0    2022
1    2022
2    2022
3    2023
4    2023
Name: date, dtype: int64
'''
print("월수")
print(df['date'].dt.month)
'''
월수
0    10
1    11
2    12
3     1
4     2
Name: date, dtype: int64
'''
print("일수")
print(df['date'].dt.day)
'''
0    31
1    30
2    31
3    31
4    28
Name: date, dtype: int64
'''
print('5. 날짜 ---> 문자')
print(df['date'],df['date'].astype(str)+'AA')
'''
4. 날짜 정보 얻기
0   2022-10-31
1   2022-11-30
2   2022-12-31
3   2023-01-31
4   2023-02-28
Name: date, dtype: datetime64[ns] 0    2022-10-31
1    2022-11-30AA
2    2022-12-31AA
3    2023-01-31AA
4    2023-02-28AA
Name: date, dtype: object
'''
