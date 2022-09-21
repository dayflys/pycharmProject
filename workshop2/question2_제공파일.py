def main():
    '''
        입력으로 제공되는 파일명 리스트를 이용하여, 확장자를 제외한 파일명을 출력하는 프로그램을 작성하시오.
        (단, 파일확장자는 마침표(.)로 구분되며 2~4문자로 구성된다. Ex : doc, docx, sh, 등)
        입력 예시1) [test.html, run.sh, report.docx, data.dat], 출력 예시1) [test, run, report, data]
        입력 예시2) [pic.png, resume.doc, test.py, index.html], 출력 예시2) [pic, resume, test, index]
    '''

    # 입력 : 파일명 리스트
    file_name_list = ["pic.png", "resume.doc", "test.py", "index.html"]
    # file_name_list = ["test.html", "run.sh", "report.docx", "data.dat"]

    split_names = []
    ####### 구현 시작 ################
    for i in range(len(file_name_list)):
        _,x = file_name_list[i].split('.')
        split_names.append(x)
    ########구현 끝 #######################
    print("-------------------------------------------------------------------------------")
    print("확장자를 제외한 파일명 목록 : ", split_names)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
