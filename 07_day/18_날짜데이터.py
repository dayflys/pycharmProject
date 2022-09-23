'''
    날짜 데이터

    from datetime import datetime
'''

from datetime import datetime

# print(dir(datetime))

'''
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__'
, '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__'
, '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__'
, '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__'
여기서 부터 함수 
, 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar'
, 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat'
, 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution'
, 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today'
, 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple'
, 'weekday', 'year']
'''

print("1. 현재날짜: ",datetime.now())#1. 현재날짜:  2022-09-23 17:32:24.836730
print("1. 현재날짜: ",datetime.today())#1. 현재날짜:  2022-09-23 17:32:24.836753
print("2. 연도만 출력: ",datetime.today().year)#2. 연도만 출력:  2022
print("2. 월만 출력: ",datetime.today().month)#2. 월만 출력:  9
print("2. 일만 출력: ",datetime.today().day)#2. 일만 출력:  23
print("2. 시간만 출력: ",datetime.today().hour)#2. 시간만 출력:  17
print("2. 분만 출력: ",datetime.today().minute)#2. 분만 출력:  34
print("2. 밀리초만 출력: ",float(datetime.today().second))#2. 밀리초만 출력:  48

#특정 날짜 설정 (2002년 05월 06일)
new_date = datetime(2002,5,6,17,34,39)
new_date2 = datetime(2002,5,6, minute=17, second=34)
time_dict = {
    'year':2002,
    "month":5,
    "day":6
}
new_date = datetime(**time_dict) # ==> **time_dict = (year = 2002 ,month = 5 ,day = 6)
print(new_date.year)#2002
print(new_date)#2002-05-06 17:34:39 => 전부 할당
print(new_date2)#2002-05-06 00:17:34 => named 파라미터 사용
