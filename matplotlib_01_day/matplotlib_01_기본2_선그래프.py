'''

    시각화 방법
    1. matplotlib 라이브러리 이용
    2. seaborn 라이브러리 이용 (matplotlib 기반)
    3. pandas 시각화 (matplotlib 기반)

    pip install matplotlib

    import matplotlib.pyplot as plt
'''

import matplotlib.pyplot as plt

#도화지 얻기
fig = plt.figure()

#하나의 붓 얻기
ax = plt.axes()
ax.plot([1,2,3,4]) #y값 의미, x값은 자동으로 설정
ax.plot([6,5,7,2]) #y값 의미, x값은 자동으로 설정
#시각화 완료
plt.show()
