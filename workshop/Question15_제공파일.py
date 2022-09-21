
def main():
    '''
     9.	다음과 같이 문자와 수치 데이터를 입력 받아서 각각의 개수를 출력하는 코드를 작성하시오.


    입력: hello world! 123

    출력: LETTERS: 10
         DIGITS: 3

    '''
    input_data = "hello world! 123"
    letters = 0
    digits = 0

    ####### 구현 시작 ################
    letter = list(input_data.strip().split())
    for l in letter:
        if l.isnumeric():
            digits += len(l)
        else:
            letters += len(l)

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("LETTERS:", letters)
    print("DIGITS:", digits)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
