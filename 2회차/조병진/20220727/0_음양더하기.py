# 음양 더하기
# 문제 : 정수를 담은 리스트와 불리언을 담은 리스트를 비교한다.
#       참이면 더하고, 거짓이면 빼서 결과값 출력

def solution(absolutes, signs):

    result = 0
    for i in range(len(signs)):
        if signs[i] == True:
            result += absolutes[i]
        else:
            result -= absolutes[i]

    return result
