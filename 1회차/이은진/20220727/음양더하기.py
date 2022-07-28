def solution(absolutes, signs):
    for i in range(len(absolutes)):
        true_num = []
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
        true_num.append(absolutes[i])
    answer= sum(true_num)
    return answer

print(solution([4,7,12], [True, False, True]))