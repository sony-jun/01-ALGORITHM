def solution(absolutes, signs) :
    for num in range(len(absolutes)) :
        if signs[num] == False :
            absolutes[num] = -absolutes[num]
    answer = sum(absolutes)

    return answer