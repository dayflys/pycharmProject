'''
    파일 쓰기

'''

#1. 쓰기 => 파일이 없으면 자동으로 생성된다.

with open('./resourse/bbb.txt','w',encoding='utf-8') as f:
    f.write('world\n')

#2. 쓰기 => 파일이 없으면 자동으로 생성된다."a"모드는 덮어쓰기 됨.
with open('./resourse/bbb.txt','a',encoding='utf-8') as f:
    f.write('world \n')



#3. 쓰기 => print() 함수 이용
with open('./resourse/bbb2.txt','a',encoding='utf-8') as f:
    print('world \n', file=f)

#3. 쓰기 => f.writelines(['a','b','c',...])
with open('./resourse/bbb3.txt','w',encoding='utf-8') as f:
    xx =['AAAA','BBBB','CCCCC']
    xx = "\n".join(xx)#라인 바꾸기 작업
    f.writelines(xx)

#python -m pip install cx_Oracle --upgrade




with open('./resourse/bbb3.txt','r',encoding='utf-8') as f:
    line =f.read()
    print(line)