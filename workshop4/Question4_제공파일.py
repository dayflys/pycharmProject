def main():
    '''
    2. 입력으로 제공되는 목록의 각 상품정보(상품명:금액)를 지정된 형식으로 변환하는 프로그램을 작성하시오.
        (단, 출력 순서는 고려하지 않으며, 변환시에 공백을 포함시키지 않는다.)
        *변환 형식: 상품명-가격:금액, 예) monitor:10000 -> monitor-price:10000

입력1) {"monitor": 100000, "mouse": 3000, "notebook": 800000, "keyboard": 9800}
출력1) {'monitor-price': 100000, 'mouse-price': 3000, 'notebook-price': 800000, 'keyboard-price': 9800}
입력2) {"mouse":150000, "keyboard":138000, "pointer":80000, "battery":19900}
출력2) {'mouse-price': 150000, 'keyboard-price': 138000, 'pointer-price': 80000, 'battery-price': 19900}

    '''

    # 입력 : 상품 정보(상품명:금액) 목록
    products = {"monitor": 100000, "mouse": 3000, "notebook": 800000, "keyboard": 9800}
    products =  {"mouse":150000, "keyboard":138000, "pointer":80000, "battery":19900}

    temp_dict = {};
    ####### 구현 시작 ################

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("변환 결과 : ", temp_dict)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
