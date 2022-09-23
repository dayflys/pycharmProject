
#접근을 당하는 모듈(target file)

#module02.py


class Dog:
    def __init__(self):
        print('module01 Dog 생성자')
        print(__name__)#mymodule.module02

def fun2():
    print('fun')

num = 30
num2 = 20

print(id(Dog))
#여지껏 위에서 만든 요소들 접근은 같은 파일에서 했었다.