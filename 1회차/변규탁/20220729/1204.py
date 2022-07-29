import sys

sys.stdin = open("1204_input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    N = int(input())
    score_list = dict()
    scores = map(int, input().split())
    # 스코어들을 score_list에 개수세기
    for score in scores:
        if score in score_list:
            score_list[score] += 1
        else:
            score_list[score] = 1

    rank_1 = max(score_list.values())
    list_ = []
    
    for k, v in score_list.items():
        if v == rank_1:
            list_.append(k)

   
    print(f'#{test_case} {list_[0]}')