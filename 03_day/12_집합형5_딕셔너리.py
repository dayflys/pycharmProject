"""
    집합형
        딕셔너리
        ->표현: {key:value, name:value}
                dict(key=value, key=value) ==> (******)
                dict(중첩리스트)==> dict([['key','value'],['key',리스트]])
        -> 타입:type({key:value}) => <class 'dict'>
                            =>딕셔너리는 class 로 만들어짐
                            =>클래스 구성요소(변수, 함수)
        -> 특징: 다른 집합형(문자열,리스트,튜플,셋)은 값만 저장해서 사용함.
            -> 딕셔너리는 key:value 혁시으로 저장해서 사용함.
                => key값만 알면 value값을 바로 조회 할 수 있다. 검색 속도가 굉장히 빠르다.
                => key를 이용해서 value값을 관리한다.(조회, 삭제, 수정)



        -> 함수 정리
        print(dir(dict))
"""

#print(dir(dict))
'''
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__'
, '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__'
, '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__'
, '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__'
, '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__'
, '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__'
여기서 부터 함수
, 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault'
, 'update', 'values']
'''

#1.dict 생성
m= {"name": "홍길동","age": 20}# key:value 에서는 "key"처럼 "" 필수
m2= dict(name='홍길동',age=20) # key=value 에서는 "" 지정하면 안됨
m3=dict([['name','홍길동'],['age',20]]) #{'name': '홍길동', 'age': 20} {'name': '홍길동', 'age': 20} {'name': '홍길동', 'age': 20}
print(m,m2,m3)

#2. 조회 ==> m["key"]
m= {"name": "홍길동","age": 20}
print(m['name'],m['age'])#홍길동 20
#print(m["address"]) #존재하지 않는 key 지정시 KeyError 발생

#2. 조회2 ==> m.get("key")
m= {"name": "홍길동","age": 20}
print(m.get('name'),m.get('age'))#홍길동 20
print(m.get("address",)) #None 존재하지 않는 key 지정시 None값 출력
print(m.get("address","서울")) #"서울" 존재하지 않는 key 지정시 default값 출력
# help(m.get) #get(key, default=None, /)

#2. 조회3 ==> key만 얻기, m.keys()
m= {"name": "홍길동","age": 20,'address':'서울'}
keys =  m.keys()
print(keys) #dict_keys(['name', 'age'])
print(list(keys)) #['name', 'age']
for key in list(keys):
    print(key,m.get(key),m[key]) #name 홍길동 홍길동  age 20 20

#2. 조회4 ==> value만 얻기, m.values()
m= {"name": "홍길동","age": 20,'address':'서울'}
values = m.values()
print(values) #dict_values(['홍길동', 20, '서울'])
print(list(values)) # ['홍길동', 20, '서울']
for value in list(values):
    print(value) #20  서울

# 2. 조회5 ==> key,value 얻기, m.items()
m = {"name": "홍길동", "age": 20, 'address': '서울'}
items = m.items()
print(items) #dict_items([('name', '홍길동'), ('age', 20), ('address', '서울')])
print(list(items)) # [('name', '홍길동'), ('age', 20), ('address', '서울')]
for x in list(items):
    print(x, end=",") #('name', '홍길동'),('age', 20),('address', '서울')

for k,v in list(items): #items 사용시 이걸 가장 많이 씀
    print(k ,':',v) #name : 홍길동  age : 20  address : 서울

for k, v in items:  # items 사용시 이걸 가장 많이 씀, list를 굳이 안써도 됨
    print(k, ':', v)  # name : 홍길동  age : 20  address : 서울

#3.추가, m[새로운 key] = 값 => 없는 key값인 경우
m = {"name": "홍길동", "age": 20}
m['address']='서울'
print(m) #{'name': '홍길동', 'age': 20, 'address': '서울'}

#4.수정 m[존재하는 key] = 값 => 존재하는 key값인 경우
m = {"name": "홍길동", "age": 20}
m['age']= 30
print(m)#{'name': '홍길동', 'age': 30}

# 추가와 수정 차이는 key값의 존재 여부다. 존재하면 수정, 존재하지 않으면 추가가 된다.

#4. 수정2 - update (): 병합 가능 => 존재하지 않는 값이면 추가와 같다.
m = {"name": "홍길동", "age": 20}
#help(m.update) #D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#m.update({key:value,key:value}) #E
#m.update({key=value,key=value}) #F
m.update({"address":'서울'}) # 추가와 결과가 같다.
print(m) #{'name': '홍길동', 'age': 20, 'address': '서울'}

#4. 수정3 - update (): 병합 가능 => 존재하는 값이면 수정과 같다.
m = {"name": "홍길동", "age": 20}
m.update({"name": "이순신", "age": 30})
print(m) #{'name': '이순신', 'age': 30}

#4. 수정4 - update (): 병합 가능 => 2,3 둘다 사용 가능하다
m = {"name": "홍길동", "age": 20}
m.update({"name": "이순신", "age": 30, 'email':'lee@google.com'})
print(m) #{'name': '이순신', 'age': 30, 'email': 'lee@google.com'}

#5. 삭제 - pop, clear
m = {"name": "홍길동", "age": 20}
m.pop("age")
print(m) #{'name': '홍길동'}
m.clear()
print(m)#{} <- 비어있는 중괄호는 dict이다.
