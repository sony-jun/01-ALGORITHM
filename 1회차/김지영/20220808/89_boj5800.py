# 각 반 수학 시험 성적의 통계
# input = 각 반 학생들의 수학 시험 성적
# output = 최대 점수 최소 점수, 점수 차이
T = int(input())
for test_case in range(1,T+1):
    scores = list(map(int,input().split()))
    n = scores[0]
    scores = scores[1:]
    scores.sort()
    gap_lst = []
    for i in range(n-1):
        gap = scores[i+1]-scores[i]
        gap_lst.append(gap)
    # print(gap_lst)
    
    max_result = max(scores)
    min_result = min(scores)
    max_gap = max(gap_lst)
    print(f'Class {test_case}')
    print(f'Max {max_result}, Min {min_result}, Largest gap {max_gap}')