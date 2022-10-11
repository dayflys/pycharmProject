'''

    시각화 방법
    1. matplotlib 라이브러리 이용
    2. seaborn 라이브러리 이용 (matplotlib 기반)
    3. pandas 시각화 (matplotlib 기반)

    pip install matplotlib

    import matplotlib.pyplot as plt

    *figyre와 axes를 한꺼번에 얻기
    plt.subplots()
    후에
    ax[index].plot()
    or
    plt.plot() --> 이걸 쓰면 마지막에 추가됨

    *하나의 figure(도화지, Canvas역할) 안에 여러 axes 생성 ==> 배열로 반환
'''

import matplotlib.pyplot as plt

fig,ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot([1,2,3,4]) #y값 의미, x값은 자동으로 설정
ax[1].plot([6,5,7,2]) #y값 의미, x값은 자동으로 설정
plt.show()
