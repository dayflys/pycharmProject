'''
    빌트인(built-ins) 함수(내장함수)

'''
"""
'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 
  'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 
  'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod',
   'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset',
    'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
     'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map',
      'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
    'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'"""

print("1.합계:", sum([1,2,3,4]))#1.합계: 10
n = [1,2,3,4]
print("2.평균:", sum(n)/len(n))#2.평균: 2.5
print("3.최댓값:", max(10,4))#3.최댓값: 10
print("3.최댓값:", max(10,4,20))#3.최댓값: 20
print("3.최댓값:", max([1,2,34,99]))#3.최댓값: 99
print("3.최댓값:", max({10:'aa',20:'bb',7:'xxx'}))#3.최댓값: 20
print("4.최솟값:", min(10,4))#4.최솟값: 4
print("4.최솟값:", min(10,4,20))#4.최솟값: 4
print("4.최솟값:", min([1,2,34,99]))#4.최솟값: 1
print("4.최솟값:", min({10:'aa',20:'bb',7:'xxx'}))#4.최솟값: 7

#문제: 인구수가 큰 순서대로 정렬하시오
x = {'서울':1000, '경기':1500, '부산':800}
print(max(x, key=lambda y:x[y]))

print("5.절댓값:", abs(-10),abs(10))#5.절댓값: 10 10
print("6.모두 참인 값인지:", all([10,'aa',True]))#6.모두 참인지: True
print("6.모두 참인 값인지:", all([10,'aa',True,0,'']))#6.모두 참인지: False
print("7.하나라도 참인 값이 있는지:", any([10,'',[],None]))#7.하나라도 참인 값이 있는지: True
print("7.하나라도 참인 값이 있는지:", any([0,'',[],None]))#7.하나라도 참인 값이 있는지: False
n=10
n2=20
print("8. (문자열 표현식을 연산해준다)eval:", eval('n+n2'))#8. eval: 30
print("8. (문자열 표현식을 연산해준다)eval:", eval('n>n2'))#8. eval: False
print("8. (문자열 표현식을 연산해준다)eval:", eval('n<n2'))#8. eval: True
print("9. 반올림을 해준다:", round(10.87))#9. 반올림을 해준다: 11
print("9. 반올림을 해준다:", round(10.87,1))#9. 반올림을 해준다: 10.9

