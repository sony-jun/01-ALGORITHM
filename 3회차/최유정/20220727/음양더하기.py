#https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0 
    for i in range(len(absolutes)):
        if signs[i] is True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        print(answer)
    return answer


