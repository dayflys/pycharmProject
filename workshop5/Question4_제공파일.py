# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------

import numpy as np


# #제공 함수 수정 금지
def main():
    # 입력 : (4 X 4)) 정수 리스트
    num = [[1, 2, 3, 4], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16, 17]]
    # num = [[-1, 2, -3, 4], [-6, 17, 18, 19], [-10, 11, -12, 13], [14, 15, 16, -17]]

    #  (4 X 4) 정수 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 짝수열(0과 2)만 추출하여 1차원 벡터로 변환하는 함수 get_vector() 호출
    #  get_vector()함수 응시생 구현
    result_vector = get_vector(num)

    # 짝수열 추출후 변환된 벡터 데이터를 출력
    print_result(result_vector)


# # 응시생 구현 함수
# (4 X 4) 정수 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 짝수열(0과 2)만 추출하여 1차원 벡터로 변환하는 기능
#
# @param		num		입력데이터(정수 리스트)
# @return				    ndarray 행렬의 짝수열을 추출하여 변환된 1차원 벡터
def get_vector(num):

    temp_vector = np.array(num)[:,[0,2]].reshape(-1)
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
    print("짝수열 추출하여 변환된 벡터 데이터: ", data)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
