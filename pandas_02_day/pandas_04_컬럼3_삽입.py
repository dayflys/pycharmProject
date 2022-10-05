'''
    DataFrame에 컬럼 삽입

    1. df.insert()

'''
import pandas as pd

dict_value =   {'국어': [4,5,6,7,8]
                ,'수학': [14,35,26,8,3]}

df = pd.DataFrame(dict_value)
df.insert(1,'영어',[43,50,61,3,56])
df.insert(1,'영어',[43,50,61,3,56],allow_duplicates=True) #기본은 allow_duplicates=False 이기 때문에 에러가 날수 있다.
print(df)
'''
   국어  영어  수학
0   4  43  14
1   5  50  35
2   6  61  26
3   7   3   8
4   8  56   3
'''
'''
   국어  영어  영어  수학
0   4  43  43  14
1   5  50  50  35
2   6  61  61  26
3   7   3   3   8
4   8  56  56   3
'''