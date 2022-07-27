#https://school.programmers.co.kr/learn/courses/30/lessons/76501
#실제 정수의 합 구하기

def solution(absolutes, signs):
    ints = []
    #인덱스로 매칭해서 T/F로 부호 붙이기
    #부호 붙인 값들 합 구해서 반환
    for i in range(len(absolutes)):
        if signs[i] == False:
            ints.append(-(absolutes[i]))
        if signs[i] == True:
            ints.append(absolutes[i])
    
    answer = sum(ints)
    return answer

absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))