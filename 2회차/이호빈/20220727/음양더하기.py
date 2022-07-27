def solution(absolutes, signs):
    result = [] #결과값을 담을 리스트
    m = False
    for i in range(len(absolutes)): #인덱스 접근을 위해서 range함수를 사용
        pair = (absolutes[i], signs[i]) #절대값과 배열을 하나로 묶는다
        if pair[1] == m: # 만약에 signs에 담겨져 있는 수가 False랑 일치하면
            result.append(-pair[0]) # 양수에서 음수로 바꿔주고
        else:
            result.append(pair[0]) # 아니면 양수 그대로 리스트에 넣는다
    return sum(result) # sum함수를 사용해서 최종 값을 출력했다.