'''
    랜덤값 이용
    1. 문법
     ->np.random.함수
'''
from pprint import pprint

import numpy as np

#1. np.random.함수
'''
['BitGenerator', 'Generator', 'MT19937', 'PCG64', 'PCG64DXSM', 'Philox', 'RandomState'
, 'SFC64', 'SeedSequence', '__RandomState_ctor', '__all__', '__builtins__', '__cached__'
, '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__'
, '_bounded_integers', '_common', '_generator', '_mt19937', '_pcg64', '_philox', '_pickle'
, '_sfc64'

, 'beta', 'binomial', 'bit_generator', 'bytes', 'chisquare', 'choice', 'default_rng'
, 'dirichlet', 'exponential', 'f', 'gamma', 'geometric', 'get_state', 'gumbel', 'hypergeometric'
, 'laplace', 'logistic', 'lognormal', 'logseries', 'mtrand', 'multinomial', 'multivariate_normal'
, 'negative_binomial', 'noncentral_chisquare', 'noncentral_f', 'normal', 'pareto', 'permutation'
, 'poisson', 'power', 'rand', 'randint', 'randn', 'random', 'random_integers', 'random_sample'
, 'ranf', 'rayleigh', 'sample', 'seed', 'set_state', 'shuffle', 'standard_cauchy'
, 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'test'
, 'triangular', 'uniform', 'vonmises', 'wald', 'weibull', 'zipf']

 '''
# print(dir(np.random))
np.random.seed(1234)
#1. np.random.random(), 0.0 <= < 1.0
print("1. np.random.random()") #def random(size: Any = None) -> None
print(np.random.random()) #0.1915194503788923
print("2. np.random.random(갯수)")
print(np.random.random(5))#[0.62210877 0.43772774 0.78535858 0.77997581 0.27259261] => 여러개를 가져올 수도 있다.
print('*'*100)

#2. np.random.rand(), 균등 분포에서 랜덤값 추출
print("3. np.random.rand([갯수])") #def rand(*dn: Any) -> Any, 균등 분포에서 랜덤값 추출
print(np.random.rand()) #0.2764642551430967
print(np.random.rand(5))#[0.80187218 0.95813935 0.87593263 0.35781727 0.50099513] => 여러개를 가져올 수도 있다.
print('*'*100)
#3. np.random.randn(), 표준 정규 분포(정규 분포중 평균값이 0이고 표준 편차가 1)에서 랜덤값 추출
print("4. np.random.randn([갯수])") #def randn(*dn: Any) -> float, 균등 분포에서 랜덤값 추출
print(np.random.randn()) #1.150035724719818
print(np.random.randn(5))#[ 0.99194602  0.95332413 -2.02125482 -0.33407737  0.00211836] => 여러개를 가져올 수도 있다.
print('*'*100)
#4. np.random.randint(),
print("5. np.random.randint()")
# #def def randint(low: int | ndarray | Iterable | float[int],
#             high: int | ndarray | Iterable | float[int] | None = None,
#             size: int | Iterable | tuple[int] | None = None,
#             dtype: object | None = None) -> int, 반드시 low 값을 지정해야 한다.
print(np.random.randint(2)) #0
print(np.random.randint(2, size=5))#[0 0 1 1 1] => 0~최대 2 범위 안에서 5개의 정수 반환(2는 포함이 안 된다) 여러개를 가져올 수도 있다, 중복 추출도 가능하다.
print(np.random.randint(1,10, size=5))#[1 1 4 3 4] =>1~10 사이의 정수값 중에서 5개를 랜덤하게 반환(중복 추출 가능) 여러개를 가져올 수도 있다, 중복 추출도 가능하다.
print('*'*100)
#5. np.random.choice(),
print("6. np.random.choice()") #지정된 리스트에서 랜덤값 추출(중복 추출 가능)
# def choice(a: Any,
#            size: int | Iterable | tuple[int] | None = None,
#            replace: bool | None = True,
#            p: Any = None) -> Any
print(np.random.choice([3,6,8,9])) #3 => size 미지정시 값 하나 반환
print(np.random.choice([3,6,8,9],size=2)) #[6 9] => size 지정시 갯수만큼 반환
print(np.random.choice([3,6,8,9],size=2, replace=False)) #[3 6] => replace = False 시 중복 추출을 금지함
print('*'*100)
#6. np.random.shuffle(),
print("6. np.random.shuffle()") #지정된 리스트에서 랜덤값 추출(중복 추출 가능)
# def shuffle(x: ndarray) -> None #in-place => 자기 자신이 변경, 복사본을 생성하지 않음
x = [1,2,3,4,5]
np.random.shuffle(x)
print(x) #[2, 3, 1, 5, 4]
print('*'*100)