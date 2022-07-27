def solution(absolutes, signs):
    
    for position in range(len(absolutes)):
        if signs[position]:
            absolutes[position] = absolutes[position]
        else:
            absolutes[position] *= -1
    
    answer = sum(absolutes)
    return answer