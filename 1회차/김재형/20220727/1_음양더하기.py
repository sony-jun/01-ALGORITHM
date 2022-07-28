# absolutes = 절대값을 차례대로 담은 정수
# signs = 정수들의 부호를 차례대로 담은 불리언

def solution(absolutes, signs):
    
    answer = 0
    
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
                   
    answer = sum(absolutes)
                   
    return answer