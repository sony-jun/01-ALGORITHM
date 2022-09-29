# 음양더하기

def solution(absolutes, signs):
    # signs가 참이면 해당 absolutes의 수가 양수, 거짓이면 음수
    # absolutes를 합한 전체값
    answer = 0 
    for i in range(len(absolutes)):
        #  true인경우 양수이므로 더하기
        if signs[i] == 'true':
            answer += absolutes[i]
        # false인 경우 음수이므로 빼기
        else:
            answer -= absolutes[i]
    return answer

print(solution([4, 7, 12], ['true', 'false', 'true']))
print(solution([1, 2, 3], ['false', 'false', 'true']))