import sys
import collections

sys.stdin = open("0_SASA 모형을 만들어보자.txt")
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    answer = sum(absolutes)
    return answer

print(solution([4,7,12],[True,False,True]))
print(solution([1,2,3],[False,False,True]))
