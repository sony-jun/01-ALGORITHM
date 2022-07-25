# https://school.programmers.co.kr/learn/courses/30/lessons/68644

#풀이 1
def solution(numbers):
    answer = []

    for i in range(len(numbers)) :
      for num in range(i + 1, len(numbers)) :
        answer.append(numbers[i] + numbers[num])
    
    answer = list(set(answer))
    answer.sort()
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

# 풀이 2
from itertools import combinations

def solution1(numbers) :
    answer1 = []

    for num in combinations(numbers, 2) :
        answer1.append(sum(num))

    answer1 = list(set(answer1))
    answer1.sort()
    return answer1

    
print(solution1([2, 1, 3, 4, 1]))
print(solution1([5, 0, 2, 7]))