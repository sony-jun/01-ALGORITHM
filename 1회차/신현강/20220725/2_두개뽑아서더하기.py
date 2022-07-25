# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    l=len(numbers)
    answer = []
    index=0
    for i in range(l-1):
        for j in range(i+1, l):
            answer.append(numbers[i] + numbers[j])
            
    answer=list(set(answer))
    answer.sort()
    return answer
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
