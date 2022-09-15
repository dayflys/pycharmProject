'''
     변수에 저장된 데이터의 타입 비교
     None 타입 비교시 isinstance() 사용 불가, is None 연산자를 대신 사용한다.
'''
int_value = 10
none_value = None
print("int_value 변수에 저장된 데이터타입이 int가 맞아?", isinstance(int_value,int))
print("int_value 변수에 저장된 데이터타입이 str가 맞아?", isinstance(int_value,str))
print("none_value 변수에 저장된 데이터타입이 none이 맞아?", none_value is None)

string_value= "hello"
list_value=[10,20]
tuple_value = (10,20)
set_value = {10,20}
dict_value = {'name': '홍길동', 'age': 20}

print("str_value 변수에 저장된 데이터타입이 str가 맞아?", isinstance(string_value,str))
print("list_value 변수에 저장된 데이터타입이 list가 맞아?", isinstance(list_value, list))
print("tuple_value 변수에 저장된 데이터타입이 tuple가 맞아?", isinstance(tuple_value, tuple))
print("set_value 변수에 저장된 데이터타입이 set가 맞아?", isinstance(set_value,set))
print("dict_value 변수에 저장된 데이터타입이 dict가 맞아?", isinstance(dict_value,dict))
