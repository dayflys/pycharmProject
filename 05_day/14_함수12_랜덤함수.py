'''
    랜덤함수

    1. import random(패키지) 꼭 명시해야 한다.
    2. 랜덤함수 사용?
        random.함수명

'''

import random

# print(dir(random))

'''
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom',
 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__'
 , '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos'
 , '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite'
 , '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test'
 , '_test_generator', '_urandom', '_warn'
 여기서 부터 함수
 , 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate'
 , 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate'
 , 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample'
 , 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
'''

print('0.random.seed() = 랜덤값 고정 ')
print(random.seed(20))

# help(random.seed) #seed(a=None, version=2) method of random.Random instance

print('1. random.randint(a,b)')
print(random.randint(1,3)) #1~3 사이의 값을 랜덤하게 변환

# help(random.random) #random() -> x in the interval [0, 1)

print('2. random.random[0,1)')
print(random.random())

# help(random.randrange) #Choose a random item from range(start, stop[, step]).

print('3. random.randrange[0,)')
print(random.randrange(1,3)) #1~2사이의 랜덤값 반환
print(random.randrange(1,10,2))#1,3,5,7,9 사이의 랜덤값 반환
# print(random.randrange(1.5,3.6))#정수값만 사용가능

print('4.random.choice(집합형 중에 하나를 랜덤하게 뽑아낸다) ')
print(random.choice(['A',"B",'C']))


print('5.random.shuffle(집합형을 랜덤하게 섞는다) ')
xxx = ['A',"B",'C']
random.shuffle(xxx)
print(xxx)

