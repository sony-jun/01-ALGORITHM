# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for j in range(0, len(numbers)):
        for i in range(0, len(numbers)):
            if i != j:
                answer.append(numbers[j] + numbers[i])
    
    removedup = set(answer)
    answer = list(removedup)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
