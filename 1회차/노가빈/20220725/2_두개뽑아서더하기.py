# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    numList = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j :
                n = numbers[i] + numbers[j]
                numList.append(n)
    numList = sorted(set(numList))     
    
    return numList


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
