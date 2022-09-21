
def main():
    '''
        입력으로 제공되는 문자열 목록의 각 문자열의 길이가 10이상이면 10문자만 남기고 나머지 문자는 …(마침표3개)로 변환하는 프로그래밍을 작성하시오.
        입력1) certification, Programming Languages, Algorithms to Live, Web Development
        출력1) certificat…, Programmin…, Languages, Algorithms…, Web Develo…
        입력2) Data Scientist,intelligence,Python Programming,Machine Learning,artificial intelligence
        출력2) Data Scien..., intelligen..., Python Pro..., Machine Le..., artificial...
    '''

    # 입력 : 문자열 목록
    words = ["certification", "Programming", "Languages", "Algorithms to Live", "Web Development"]
    # words = ["Data Scientist", "intelligence", "Python Programming", "Machine Learning","artificial intelligence" ]

    changed_list = []
    ####### 구현 시작 ################
    changed_list = [word[:9]+'...' if len(word) > 10 else word for word in words]
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("변환 결과 : ", changed_list)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
