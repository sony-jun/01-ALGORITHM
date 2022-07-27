def solution(absolutes, signs):
    # absolutes = [4, 7, 12], signs = [true,false,true]
    answer = 0
    for i in range(len(absolutes)):
        if (absolutes[i] and (signs[i])) == 1:
            answer += absolutes[i]
        elif (absolutes[i] and (signs[i])) == 0:
            answer -= absolutes[i]

    return answer