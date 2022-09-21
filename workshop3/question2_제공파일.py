def main():
    '''
    입력으로 제공되는 이름 목록에서 이름이 ‘A’ 또는 ‘a’로 시작하는 이름의 개수를 계산하는 프로그램을 작성하시오.
입력 예시1) "Alis", "James", "Martin", "aim", "John", "atom", "adam", "chris", "dan", 출력 예시1) 4
입력 예시2) "Jimmy", "Mars", "Peter", "John", "Alis", "edan", "Call", 출력 예시2) 1

    '''
    # 입력 : 튜플 데이터(이름 튜플)
    name_tuple =("Alis", "James", "Martin", "aim", "John", "atom", "adam", "chris", "dan")
    # name_tuple =("Jimmy", "Mars", "Peter", "John", "Alis", "edan", "Call")

    start_character = "A";

    count = 0
    ####### 구현 시작 ################
    for i in name_tuple:
        if i[0].upper() == 'A':
            count +=1
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("이름이 A또는 a로 시작하는 사람 수 : ", count)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
