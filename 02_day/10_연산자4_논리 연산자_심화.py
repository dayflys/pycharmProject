'''
n값이 10보다 작고 4보다 크냐?
'''
n=3
print(4<n<10) #다른 언어는 이렇게 쓸수 없다. 권장 하지는 않는다.
print( (n < 10) and (n >4))

print("일반데이터(일반형/집합형)가 False로 변환되는 경우") #--> 0과 None,빈 자료형이면 False 이다.
print(0,bool(0))#False
print(0.0,bool(0.0))#False
print(None,bool(None))#False

print('',bool(''))#False
print([],bool([]))#False
print((),bool(()))#False
print({},bool({}))#False --> 비어있는 중괄호는 기본적으로 dict로 처리 한다.

print("일반데이터(일반형/집합형)가 True로 변환되는 경우")# --> 0이 아니면 True이다.
print(10,bool(10))#True
print(3.14,bool(3.14))#True

print("A",bool("A"))#True
print([1],bool([1]))#True
print((1,),bool((1,)))#True
print({1},bool({1}))#True
