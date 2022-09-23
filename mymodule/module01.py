
#접근을 당하는 모듈(target file)

#module01.py

class Cat:
    def __init__(self):
        print('module01 Cat 생성자')
        print(__name__) #mymodule.module01

def fun():
    print('fun')

num = 10

print(id(Cat))
#여지껏 위에서 만든 요소들 접근은 같은 파일에서 했었다.