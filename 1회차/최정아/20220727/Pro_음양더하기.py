def solution(absolutes, signs):

    for i in range(len(absolutes)) :
        if signs[i] == True :
            absolutes[i] = absolutes[i]
        else :
            absolutes[i] = absolutes[i] - (absolutes[i]*2)

    answer = sum(absolutes)

    return answer