'''

    시각화 방법
    1. matplotlib 라이브러리 이용
    2. seaborn 라이브러리 이용 (matplotlib 기반)
    3. pandas 시각화 (matplotlib 기반)

    pip install matplotlib

    import matplotlib.pyplot as plt

    *figyre와 axes를 한꺼번에 얻기
    plt.subplots()
'''

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
ax.plot([1,2,3,4]) #y값 의미, x값은 자동으로 설정
plt.show()
