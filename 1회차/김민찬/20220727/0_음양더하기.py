def solution(absolutes, signs): # signs가 True 해당 absolutes의 수가 양수, 거짓이면 음수

    for i in range(len(absolutes)) :
        if signs[i] == True : # True -> 양수이기 때문에 그대로 나와서 더하기
            absolutes[i] = absolutes[i]
        else :                # False -> 음수이기 때문에 -붙여서 나와서 빼기
            absolutes[i] = absolutes[i] * (-1)
    
    answer = sum(absolutes)
    return answer

print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))