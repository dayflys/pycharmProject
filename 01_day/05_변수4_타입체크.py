'''

    변수에 저장된 데이터의 종류 알아보기

'''

int_value=10
float_value=3.14
bool_value = True

def fun():
    pass

func_value = fun
none_value = None

print("int_value:",int_value, type(int_value))
print("float_value:",float_value, type(float_value))
print("bool_value:",bool_value, type(bool_value))
print("func_value:",func_value, type(func_value))
print("none_value:",none_value, type(none_value))

#집합형
string_value= "hello"
list_value=[10,20]
tuple_value = (10,20)
set_value = {10,20}
dict_value = {'name': '홍길동', 'age': 20}

print("string_value:",string_value, type(string_value))
print("list_value:",list_value, type(list_value))
print("tuple_value:",tuple_value, type(tuple_value))
print("set_value:",set_value, type(set_value))
print("dict_value:",dict_value, type(dict_value))


print("int_value 변수에 저장된 데이터타입이 int가 맞아?", isinstance(int_value,int))