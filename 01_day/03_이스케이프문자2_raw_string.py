#이스케이프 문자(escape)를 무시 ==> raw string
#문자열 앞에 r을 붙히면 무시된다.

print(r'hello\nWorld')
print(r'hello\tworld')
print(r'hello\rworld')
print(r'hello\bworld')
print(r'hello\'world')
print(r'hello\"world')
print(r'hello\\world')


