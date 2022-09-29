# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------

import numpy as np
# #제공 함수 수정 금지
def main():
    # 입력 : 정수 리스트
    num = [9, -8, 7, 6, 5, 4, 7, 5, 4]
    num2 = [1, 2, 3, -4, 5, -6, -3, 2, 1]

    # num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # num2 = [23, 53, 13, 2, 1, -6, 11, 3, 5]

    #  두 개의 정수 리스트를 (3 X 3) ndarray 행렬로 각각 변환하고, 변환된 두 행렬의 행렬곱(내적)을 구하여
    #  각 요소의 결과값이 양수이면 음수로, 음수이면 양수로 변경하는 함수 get_matrix() 호출 , get_matrix()함수 응시생 구현
    result_matrix = get_matrix(num, num2)

    # 행렬곱하여 각 요소의 값이 변경된 행렬 출력
    print_result(result_matrix)


# # 응시생 구현 함수
#  두 개의 정수 리스트를 (3 X 3) ndarray 행렬로 각각 변환하고, 변환된 두 행렬의 행렬곱(내적)을 구하여
#  각 요소의 결과값이 양수이면 음수로, 음수이면 양수로 변경하는 기능
#
# @param		num		입력데이터(정수 리스트)
# @param		num2	입력데이터(정수 리스트)
# @return				    행렬곱하여 각 요소의 값이 변경된 행렬
def get_matrix(num, num2):
    num = np.array(num).reshape(3,3)
    num2 = np.array(num2).reshape(3,3)
    arr = np.dot(num,num2)
    arr = np.where(arr > 0 ,-arr,-arr)
    temp_matrix = arr
    pass
    # 응시생 구현 끝
    return temp_matrix


# #제공 함수 수정 금지
def print_line():
    print("-------------------------------------------------------------------------------")


# #제공 함수 수정 금지
def print_result(data):
    print_line()
    print("행렬곱하여 각 요소의 값이 변경된 행렬: ", data)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
