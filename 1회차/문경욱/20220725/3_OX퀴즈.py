# https://www.acmicpc.net/problem/8958
# 테스트 케이스를 입력 받음
T = int(input())

'''
for test_case in range(T): # 내 풀이 - count_o를 이용해서 
    # O와 X 문자열을 ans로 입력받음
    ans = input()
    # o를 집어넣을 o_list를 선언
    o_list = []
    # 전체 합과 임시 합을 선언
    sum_num = 0
    sum_tmp = 0

    # 입력 개수만큼 반복문 진행
    for i in range(len(ans)):

        # 문자가 'O'일 때
        if ans[i] == 'O':
            # o_list에 O를 추가
            o_list.append('O')

            # i가 마지막일 때, O인 경우 더하기가 진행이 되지 않으므로 i가 마지막인 경우 추가
            if i == len(ans)-1: 
                for i in range(1, len(o_list)+1):
                    sum_tmp += i
                sum_num += sum_tmp
        # 문자가 X일 때
        else:
            # o_list가 비어있을 때는 그냥 진행
            if len(o_list) == 0:
                continue
            # o_list가 비어있지 않을 때는
            else:
                # 1,2,3, 씩 O 갯수만큼 sum_tmp에 담아 전체 sum에 저장한 후 다시 sum_tmp를 0으로 변경, o_list 초기화
                for i in range(1, len(o_list)+1):
                    sum_tmp += i
                sum_num += sum_tmp
                sum_tmp = 0
                o_list = []
    print(sum_num)
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
O = 'O' # 고정된 입력값을 변수로 미리 저장
X = 'X' # 소문자로 입력할 경우 컴퓨터에서 알려줌!

for t in range(T):
    ox = input()
    count_o = 0
    sum_ = 0

    for answer in ox:
        if answer == O:
            count_o += 1 # 연석된 O의 개수를 증가
            sum_ = count_o + sum_

        if answer == X :
        # else: # O or X라 사용가능하지만 조건을 좀 더 명확히 하기 위함.
            count_0 = 0 ## 연속된 0의 개수를 초기화(0)

    print(sum_)