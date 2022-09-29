def solution(absolutes, signs): # 입력의 개수가 같으니 인덱스를 이용
    for i in range(len(signs)): 
        if signs[i] == False: #문제 함정이 입력에있었음
            absolutes[i] *= -1
        
    
    
    
    answer = sum(absolutes)#4 -7 12
    return answer


print(solution([4,7,12],[True,False,True]))