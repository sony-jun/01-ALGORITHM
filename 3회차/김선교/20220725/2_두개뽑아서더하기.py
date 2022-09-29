# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in numbers:
        for j in numbers:
            if i+j not in answer:
                answer.append(i+j)
    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))