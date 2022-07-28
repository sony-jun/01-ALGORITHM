def solution(absolutes, sign):
    sum_ = 0
    for i in range(0, len(absolutes)):
        if sign[i] == False:
            absolutes[i] = -absolutes[i]
        sum_ += absolutes[i]

    return sum_     
    
 
print(solution([4,7,12], 3,[True,False,True]))
print(solution([1,2,3], 3,[False,False,True]))

