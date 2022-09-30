'''
    랜덤함수 이용한 중첩리스트
'''

import numpy as np
import pandas as pd

print('1. np.random.random()')
df = pd.DataFrame(np.random.random((2,3)), columns=['A','B','C'])
print(df)
'''
          A         B         C
0  0.257815  0.316607  0.472926
1  0.995431  0.101849  0.193120
'''

print('2. np.random.rand([갯수])')
df = pd.DataFrame(np.random.rand(2,3), columns=['A','B','C'])
print(df)
'''
          A         B         C
0  0.038849  0.301371  0.430429
1  0.585108  0.890476  0.436675
'''

print('3. np.random.randn([갯수])')
df = pd.DataFrame(np.random.randn(2,3), columns=['A','B','C'])
print(df)
'''
          A         B         C
0 -0.391828  0.223186 -0.061497
1  0.688480  0.677666 -0.139822
'''

print('4. np.random.randint([갯수])')
df = pd.DataFrame(np.random.randint(2,size=(2,3)), columns=['A','B','C'])
print(df)
'''
   A  B  C
0  1  1  0
1  1  0  1
'''

print('4. np.random.choice(리스트, size)')
df = pd.DataFrame(np.random.choice([3,6,7,9],size=(2,3)), columns=['A','B','C'])
print(df)
'''
4. np.random.choice([갯수])
   A  B  C
0  6  7  6
1  9  7  6

'''