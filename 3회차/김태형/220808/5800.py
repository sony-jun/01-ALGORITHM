# 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.
# 구현

K = int(input())
for i in range(1,K+1):
    score_list = list(map(int,input().split()))
    score_list.remove(score_list[0])
    score_list.sort(reverse=True)
    gaps = []
    for j in range(len(score_list)):
        gap=score_list[j-1]-score_list[j]
        gaps.append(gap)
    max_class = max(score_list)
    min_class = min(score_list)
    Largest_gap = max(gaps)
    print(f"Class {i}")
    print(f"Max {max_class}, Min {min_class}, Largest gap {Largest_gap}")