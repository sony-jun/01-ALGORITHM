T = int(input())
for test_case in range(1,T+1):

    testcase = int(input())
    score_list = list(map(int,input().split()))
    score = {}
    for i in range(1000):
        if score_list[i] not in score:
            score[score_list[i]] = 1
        else : score[score_list[i]] += 1
    result = max(score,key=score.get)
    
    print(f'#{testcase}',result)