"""
    대입연산자 심화
    1. 하나의 값을 여러 변수에 저장
    2. 여러 변수에 여러 값을 저장
    3. dict
    -저장되는 값은 key값이 저장된다.

"""

# 1. 하나의 값을 여러 변수에 한번에 저장
a = b = c = 10
print(a, b, c)

# 2.여러개의 값을 여러 변수에 한번에 저장 (unpacking)
a, b = 10, 20
a, b = (10, 20)
a, b = [10, 20]
a, b = {10, 20}

print(a, b)

a, b, c, [d, e, [f, g]] = [1, 2, 3, [9, 8, [100, 300]]]
print(a, b, c, d, e, f, g)  # 1 2 3 9 8 100 300

# 3. dict
info = {'username': '홍길동', 'age': 20}
x, y = info
print(x, y)  # username age <class 'str'>
print(info[x], info[y])  # 홍길동 20