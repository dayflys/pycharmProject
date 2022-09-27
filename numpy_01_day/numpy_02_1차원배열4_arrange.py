'''
    arange([start,] stop[,step])
    => 파이썬의 range 함수와 비슷하다 [start, stop), step=1
        => range는 무조건 정수값만 반환
    => np.arange는 지정된 값의 타입에 따라서 반환(실수도 가능 )

'''

import numpy as np

#1. np.arrange(stop) 0~ stop -1 까지의 범위의 정수 반환
print("1. np.arange(stop)")
x = np.arange(10) # 0~9 까지의 범위의 정수 반환
print(x) #[0 1 2 3 4 5 6 7 8 9]
x = np.arange(10.) # 0~9 까지의 범위의 실수 반환
print(x) #[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
x = np.arange(10, dtype=float) # 0~9 까지의 범위의 실수 반환
print(x) #[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
print("*"*100)

#2. np.arrange(start,stop) start ~ stop -1 까지의 범위의 정수 반환
print("2. np.arange(start,stop)")
x = np.arange(1,10) # 1~9 까지의 범위의 정수 반환
print(x) #[1 2 3 4 5 6 7 8 9]
x = np.arange(1,10.) # 1~9 까지의 범위의 실수 반환
print(x) #[1. 2. 3. 4. 5. 6. 7. 8. 9.]
x = np.arange(1,10, dtype=float) # 1~9 까지의 범위의 실수 반환
print(x) #[1. 2. 3. 4. 5. 6. 7. 8. 9.]
print("*"*100)

#3. np.arrange(start,stop,step) start ~ stop -1 까지 step만큼 이동하면서 범위 내의 정수 반환
print("3. np.arange(start,stop,step)")
x = np.arange(1,10,2) # 1~9 까지의 범위의 정수(2step) 반환
print(x) #[1 3 5 7 9]
x = np.arange(1,10.,2) # 1~9 까지의 범위의 실수(2step) 반환
print(x) #[[1. 3. 5. 7. 9.]
x = np.arange(1,10,2, dtype=float) # 1~9 까지의 범위의 실수(2step) 반환
print(x) #[1. 3. 5. 7. 9.]
print("*"*100)

#날짜 범위 지정 가능 ==> 나중에 날짜 데이터에 특화된 더 좋은 함수가 있다.
x = np.arange('2022-09', '2022-10', dtype='datetime64[D]') #날짜 데이터를 반환 하기 위해서는 dtype에 datetime자료형크기[포멧]
y = np.arange('2022-09', '2023-10', dtype='datetime64[M]') #날짜 데이터를 반환 하기 위해서는 dtype에 datetime자료형크기[포멧]
z = np.arange('2000-09', '2023-10', dtype='datetime64[Y]') #날짜 데이터를 반환 하기 위해서는 dtype에 datetime자료형크기[포멧]
print(x)
'''
['2022-09-01' '2022-09-02' '2022-09-03' '2022-09-04' '2022-09-05'
 '2022-09-06' '2022-09-07' '2022-09-08' '2022-09-09' '2022-09-10'
 '2022-09-11' '2022-09-12' '2022-09-13' '2022-09-14' '2022-09-15'
 '2022-09-16' '2022-09-17' '2022-09-18' '2022-09-19' '2022-09-20'
 '2022-09-21' '2022-09-22' '2022-09-23' '2022-09-24' '2022-09-25'
 '2022-09-26' '2022-09-27' '2022-09-28' '2022-09-29' '2022-09-30']
 -----------------------------------------------------------------
 D = day
 M = month
 Y = year
'''
print("*"*100)

