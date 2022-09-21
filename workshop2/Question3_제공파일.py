def main():
    '''
        입력으로 제공되는 이름 목록의 각 이름을 첫 문자만 대문자로 변환하고 나머지 문자는 소문자로 변환하는 프로그램을 작성하시오.
        입력1) john, kim, DAVID, miZ, SINAN, TIM
        출력1) John, Kim, David, Miz, Sinan, Tim
        입력2) park, LEE, SMITH, CHOI, bell, tom
        출력2) Park, Lee, Smith, Choi, Bell, Tom
    '''

    # 입력 : 이름 목록
    names = ["john", "kim", "DAVID", "miZ", "SINAN", "TIM"]
    names = ["park", "LEE", "SMITH", "CHOI", "bell", "tom"]

    changed_list = []
    ####### 구현 시작 ################
    changed_list= [i.capitalize() for i in names]
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("변환 결과 : ", changed_list)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
