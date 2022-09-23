'''

    다중 except
    -> 한 문장 안에 여러 개의 예외가 발생할 것 같다면 except문을 다중으로 작성하거나 아니면 부모 클래스로 작성하면 된다.
    -> 목적: 예외를 세밀하게 처리하는 것이 목적
    -> 첫번째 문법이 권장됨
    #다중 except문을 활용
    try:
        문장1-> ZeroDivisionError 발생 가능
        문장2-> IndexError 발생 가능
    except ZeroDivisionError as e:
        문장
    except IndexError as e1:
        문장

    혹은
    #부모 클래스 활용
    try:
        문장1-> ZeroDivisionError 발생 가능
        문장2-> IndexError 발생 가능
    except Exception as e:
        문장
'''
import traceback

try:
    n = 10
    result = 50/ n
    print(result)

    m=[1,2]
    print(m[7])

# except ZeroDivisionError as e:
#     print(e)
#
# except IndexError as e:
#     print(e)
# except Exception as e: #관례적으로 가장 마지막에는 Exception으로 예외를 처리한다.
#     print(e)
except Exception as e:
    print(e)

