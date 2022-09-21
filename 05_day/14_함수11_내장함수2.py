'''
    filter vs map

    1.filter(함수, 집합형)
    ===> 집합형에서 함수를 적용해서 조건에 일치하는 값만 반환한다.
    ===> generator 함

    2. map(함수, 집합형)
    ===> 집합형의 데이터를 가공하기 위한 함수를 적용.
        따라서 원본 데이터의 갯수만큼 출력이 나온다.

'''
x = [1,2,3,4,5,6,7,8,9,10]
#짝수만 출력
result = [ v for v in x if v%2 == 0]
print(result) #list comprehension

def even(n):
    return n%2 == 0

result = filter(even,x)
print(list(result))# filter와 일반함수 사용

result = filter(lambda n:n%2==0,x)
print(list(result)) # filter와 lambda 함수 사용

#문제: 1~100 사이 값 중에서 5의 배수이면서, 60보다 큰 값만 출력하시오
print(list(filter(lambda x: x%5==0 and x<60,[x for x in range(1,101)])))

# 문제2: "asdfef1234xhgkasog452" 중에서 알파벳문자만 필터링해서 출력하시오.
print(''.join(list(filter(lambda x:x.isalpha(),"asdfef1234xhgkasog452"))))

# help(filter) #filter(function or None, iterable) --> filter object
# help(map) #map(func, *iterables) --> map object

print('*'* 100)
print('*'* 100)
x = ['Abc','He','WED','exias',"kEB"]

def my_upper(x):
    return x.upper()

print(list(map(my_upper,x))) #일반 함수 ['ABC', 'HE', 'WED', 'EXIAS', 'KEB']

my_upper2 = lambda x:x.upper()

print(list(map(my_upper2,x)))#람다 함수를 변수에 저장 ['ABC', 'HE', 'WED', 'EXIAS', 'KEB']

print(list(map(lambda n:n.upper(),x)))#람다함수를 직접 사용 ['ABC', 'HE', 'WED', 'EXIAS', 'KEB']
print(list(map(str.upper,x)))#직접 함수를 호출 ['ABC', 'HE', 'WED', 'EXIAS', 'KEB']
print(list(map(str.lower,x)))#직접 함수를 호출 ['abc', 'he', 'wed', 'exias', 'keb']
print(list(map(str.title,x)))#직접 함수를 호출 ['Abc', 'He', 'Wed', 'Exias', 'Keb']
result = map(int,['9','44','143'])
print(list(result))#직접 함수를 호출 [9, 44, 143]
result = map(str,[9,44,143])
print(list(result))#직접 함수를 호출 ['9', '44', '143']

