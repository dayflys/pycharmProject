'''
    값으로 삭제하는 방법
    1. 삭제할 값의 위치를 얻는다.
        => np.where(arr==5) ==> arr에서 5값의 위치를 반환
    2. np.delete(arr,idx) 이용해서 삭제한다.
'''

import numpy as np


arr = np.array([9,8,7,6,5,4,3])
print("5값의 위치:", np.where(arr==5)) #5값의 위치 (array([4]),)
print("4값의 위치:", np.where(arr==4)) #5값의 위치 (array([5]),)
print("9값의 위치:", np.where(arr==9)) #5값의 위치 (array([0]),)
print("*" *100)
new_arr = np.delete(arr,np.where(arr==5))
print("5값 삭제 :", new_arr) #5값 삭제 : [9 8 7 6 4 3]
print("*" *100)
print("8과 7의값의 위치:", np.where((arr==8) | (arr==7))) #8과 7의값의 위치: (array([2, 4]),) => 다중 개수를 지정할 때는 bitwise 연산자인 | (pipeline) 을 써야한다.
new_arr = np.delete(arr,np.where((arr==8) | (arr==7)))
print("8과 7 삭제: ", new_arr) #8과 7 삭제:  [9 6 5 4 3] => fancy 형식



