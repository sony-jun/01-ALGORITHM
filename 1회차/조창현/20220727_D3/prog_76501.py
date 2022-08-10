def solution(absolutes, signs):
    ind = 0     ## 위치를 나타내주기 위해 선언
    answer = 0  ## 정수들의 합을 저장

    for i in absolutes:
        ## 부호를 확인하여 True 라면 더해주고
        if signs[ind] == True:
            answer += i
            ## index 를 키워 다음 부호확인
            ind += 1
        ## 부호를 확인하여 False 라면 빼준다
        else:
            answer -= i
            ## index 를 키워 다음 부호확인
            ind += 1
    return answer

print(solution([1, 2, 3], [False, False, False]))