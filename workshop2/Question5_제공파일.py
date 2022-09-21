
def main():
    '''
        입력으로 제공되는 도서명 목록에서 각 도서명의 앞과 뒤의 모든 공백을 제거하는 프로그램을 작성하시오. (단, 도서명 중간에 포함된 공백은 제거하지 않는다.)
        입력1) “ Design Thinking   “, “AI and the Future   “, “   Machine Learning and Deep Learning”, “Python Programming”
        출력1) ” Design Thinking”, “AI and the Future”, “Machine Learning and Deep Learning”, “Python Programming”
        입력2) "  Data Science   ", "  Artificial Intelligence and Mathematics  ", "  AI Essentials ","  Future Society"
        출력2) “Data Science”, “Artificial Intelligence and Mathematics”, “AI Essentials”, “Future Society”
    '''

    # 입력 : 도서명 목록
    books = [" Design Thinking   ", "AI and the Future   ", "   Machine Learning and Deep Learning", "Python Programming"]
    # books = ["  Data Science   ", "  Artificial Intelligence and Mathematics  ", "  AI Essentials ","  Future Society"]

    temp_list = [];
    ####### 구현 시작 ################
    temp_list = [i.strip() for i in books]

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("도서명 앞과 뒤의 공백이 제거된 도서명 목록 : ", temp_list)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
