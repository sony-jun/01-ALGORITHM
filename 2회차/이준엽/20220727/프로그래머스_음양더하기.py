def solution(absolutes, signs):
    realnums = []
    for i in range(len(signs)):
        if signs[i] == True:
            realnums.append(absolutes[i])
        else:
            realnums.append(-1*absolutes[i])
    answer = sum(realnums)
    return answer
