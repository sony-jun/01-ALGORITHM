# 5800번 성적 통계

# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 
# 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.


# 출력
# 각 반에 대한 출력은 다음과 같이 두 줄로 이루어져 있다.
# 첫째 줄에는 "Class X"를 출력한다. X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가한다.
# 둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 
# 가장 큰 인접한 점수 차이를 예제 출력과 같은 형식으로 출력한다.

import sys

# 첫째 줄에 중덕 고등학교에 있는 반의 수 K가 주어진다. 
K = int(sys.stdin.readline())

for k in range(1, K+1):
    # 다음 K개 줄에는 각 반의 학생수 N과 각 학생의 수학 성적이 주어진다. 
    g_list = list(map(int, sys.stdin.readline().split()))
    N = g_list[0]
    g_list.remove(g_list[0])
    g_list.sort(reverse = True)  # 내림차순 정렬하는~
    max_gap = 0

    for g in range(len(g_list)-1):
        if g_list[g] - g_list[g+1] > max_gap:
            max_gap = g_list[g] - g_list[g+1]

    print(f'Class {k}')
    print(f'Max {g_list[0]}, Min {g_list[-1]}, Largest gap {max_gap}')