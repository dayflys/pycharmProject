#이스케이프(escape) 문자

print('helloWorld')
print('hello\nWorld')#\n은 라인변경
print()
print('hello   world')
print('hello\tworld')#\t는 space를 3 입력한 효과와 동일, 혹은 tab을 친 효과
print('hello\rworld')#\r은 \r 뒤에 있는 것만 출력하는 효과
print('hello\bworld')#\b는 \b 앞에 있는 문자를 하나 지우는 효과
print('hello\'world')#\'는 '을 출력해주는 효과 sql에서 _,%을 와일드카드로 인식 안하게끔 하는 것처럼
print('hello\"world')#\"는 "을 출력해주는 효과 sql에서 _,%을 와일드카드로 인식 안하게끔 하는 것처럼
print('hello\\world')#\\는 \을 출력해주는 효과 sql에서 _,%을 와일드카드로 인식 안하게끔 하는 것처럼


