def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): # 앱솔루트 리스트의 길이동안
        if signs[i] == False: # signs의 값이 False면
            absolutes[i] = -absolutes[i] # absolutes[i]의 값을 역으로 치환
        answer += absolutes[i] # 계산
    
    return answer


# absolutes	 signs	             result
# [4,7,12]	 [true,false,true]	 9
# [1,2,3]	 [false,false,true]	 0