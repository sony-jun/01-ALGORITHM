# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    temp = set()

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            temp.add(numbers[i] + numbers[j])

    answer = list(temp)
    answer.sort()

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
