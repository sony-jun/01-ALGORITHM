# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    # absolutes = [4, 7, 12]
    # # signs = [True, False, True]
    for i in range(len(absolutes)):
        if signs[i] == True: # signs[i]가 참일 때 -- 양수
            answer += absolutes[i]
        else: # signs[i]가 거짓일 때 -- 음수
            answer -= absolutes[i]
        
    return answer
print(solution([4, 7, 12], [True, False, True]))