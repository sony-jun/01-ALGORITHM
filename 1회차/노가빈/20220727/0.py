from numpy import sign


def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
            if signs[i] == False :
                sum -= absolutes[i]
            else:
                sum += absolutes[i]


    answer = 123456789
    return sum

print(solution([4,7,12],[True,False,True]))