'''
    중첩 리스트
    df = pd.DataFrame(중첩리스트| 2차원 배열, columns =[])
    df = pd.DataFrame(중첩리스트| 2차원 배열, columns =[],index=[])

    ==> 2차원 배열을 만드는 방법이면 dataframe 생성이 가능하다.

'''

import numpy as np
import pandas as pd

list_value = [[4,5,6],[1,2,3],[7,5,3]] #list
arr = np.array([[4,5,6],[1,2,3],[7,5,3]]) #ndarray

df = pd.DataFrame(list_value)
print(df)
'''
   0  1  2
0  4  5  6
1  1  2  3
2  7  5  3
'''
# print(df.index) #RangeIndex(start=0, stop=3, step=1)
# print(df.columns) #RangeIndex(start=0, stop=3, step=1)
df = pd.DataFrame(list_value, columns=['a','b','c'])
print(df)
'''
   a  b  c
0  4  5  6
1  1  2  3
2  7  5  3
'''
df = pd.DataFrame(arr, columns=['a','b','c'])
print(df)
'''
   a  b  c
0  4  5  6
1  1  2  3
2  7  5  3
'''
df = pd.DataFrame(list_value, index= [10,20,30],columns=['a','b','c'])
print(df)
'''
    a  b  c
10  4  5  6
20  1  2  3
30  7  5  3
'''
df = pd.DataFrame(arr, index= ['r1','r2','r3'],columns=['a','b','c'])
print(df)
'''
    a  b  c
r1  4  5  6
r2  1  2  3
r3  7  5  3
'''

d1 = np.arange(12).reshape(3,4)
df = pd.DataFrame(d1, columns=['A','B','C','D'])
print(df)
'''
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''