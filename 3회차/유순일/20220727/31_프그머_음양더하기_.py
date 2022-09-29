def solution(absolutes, signs):
    # signs가 참이면 해당 absolutes가 양수, 거짓이면 음수.
    # 양수, 음수가 적용된 합 
    answer = 0
    for i in range(len(absolutes)): # 문제에 signs의 길이와 absolutes의 길이가 같다고함.
        # 참인 경우 양수, 더하면 된다.
        if signs[i]: # 이 코드 자체가 signs[i]가 true라는 말.
            answer += absolutes[i]
        # 참이 아닌경우 빼라. 음수니까.
        else:
            answer -= absolutes[i]
    return answer