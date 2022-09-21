def main():
    '''
    입력으로 제공되는 도서 목록의 각 도서 중에서 주어진 검색 키워드가 포함된 도서 목록을 검색하는 프로그램을 작성하시오.
    (단, 검색 키워드와 도서는 대소문자를 구분하지 않는다.)
    입력1)
      검색 키워드: data
      도서 목록: Data Processing, Data Mining, Relational Database, data-intensive application, ML/DL
    출력1) Data Procession, Data Mining, Relational Database, data-intensive

    입력2)
      검색 키워드: pro
      도서 목록: Java Programming, Data Science, Data-Modeling, Programming with Data, Python Programming
    출력2) Java Programming, Programming with Data, Python Programming
    '''

    # 입력 : 검색 키워드
    keyword = "data"
    keyword = "pro"

    # 입력 : 도서 목록
    books = ["Data Processing", "Data Mining", "Relational Database", "data-intensive application", "ML/DL"]
    books = ["Java Programming", "Data Science", "Data-Modeling", "Programming with Data", "Python Programming"]

    search_list = []

    ####### 구현 시작 ################
    search_list = [books[i] for i in range(len(books)) if keyword in books[i].lower()]

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("검색 결과 : ", search_list)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
