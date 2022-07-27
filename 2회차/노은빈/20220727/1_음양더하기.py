def solution(absolutes, signs):
    total = 0

    for i in range (len(absolutes)):   #범위 : absolutes 리스트에 들어있는 개수만큼
        if signs[i] == True:  #signs가 True라면
            total += absolutes[i]  #양의 정수
           
        else :
            absolutes[i] < 0  #signs가 False라면
            total -= absolutes[i]  #음의 정수
           
    return total    #def 함수의 결과값 반환   
    