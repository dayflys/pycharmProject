# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------

import numpy as np


# #제공 함수 수정 금지
def main():
    # 입력 : (4 X 4) 정수 리스트
    num = [[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16, 17]]
    # num = [[21, 23, 31, 3], [68, 7, 38, 6], [20, 11, 12, 9], [74, 15, 87, 13]]

    # (4 X 4) 정수 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 열단위로 데이터를 추출하여 1차원 벡터로 변환하는 함수 get_vector() 호출
    # get_vector()함수 응시생 구현
    result_vector = get_vector(num)

    # 열단위 추출후 변환된 벡터 데이터를 출력
    print_result(result_vector)


# # 응시생 구현 함수
# (4 X 4) 정수 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 열단위로 데이터를 추출하여 1차원 벡터로 변환하는 기능
#
# @param		num		입력데이터(4 X 4 정수 리스트)
# @return				1차원 벡터
def get_vector(num):
    arr,arr2,arr3,arr4 = np.hsplit(np.array(num),len(num))
    temp_vector = np.vstack((arr.reshape(-1),arr2.reshape(-1),arr3.reshape(-1),arr4.reshape(-1))).reshape(-1)
    # 응시생 구현 시작
    pass
    # 응시생 구현 끝
    return temp_vector


# #제공 함수 수정 금지
def print_line():
    print("-------------------------------------------------------------------------------")


# #제공 함수 수정 금지
def print_result(data):
    print_line()
    print("열단위 추출후 변환된 벡터 데이터: ", data)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
