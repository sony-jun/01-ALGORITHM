def solution(absolutes, signs):
    signs_pm = []
    for i in range(len(signs)):
        if signs[i] == 1:
            signs_pm.append(1)
        elif signs[i] == 0:
            signs_pm.append(-1)

    answer = 0 
    for i in range(len(absolutes)):
        answer += absolutes[i] * signs_pm[i]
    
    return answer