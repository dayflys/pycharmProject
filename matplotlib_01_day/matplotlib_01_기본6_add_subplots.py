'''

    시각화 방법
    1. matplotlib 라이브러리 이용
    2. seaborn 라이브러리 이용 (matplotlib 기반)
    3. pandas 시각화 (matplotlib 기반)

    pip install matplotlib

    import matplotlib.pyplot as plt

    *figyre와 axes를 한꺼번에 얻기
    plt.subplots()

    *하나의 figure(도화지, Canvas역할) 안에 여러 axes 생성 ==> 배열로 반환
    plt.subplots(nrow=1, ncols=2)
    plt.subplots(nrow=2, ncols=2)

    *하나의 figure(도화지, Canvas역할) 안에 여러 axes 생성 2
    fig.add_subplot(행,열,순서)
'''

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))#단위는 inch
ax1 = fig.add_subplot(1,2,1) #1행의 2열의 첫번째열
plt.plot([1,2,3,4])


ax2 = fig.add_subplot(1,2,2) #1행의 2열의 첫번째열
plt.plot([6,5,7,2])

plt.show()
