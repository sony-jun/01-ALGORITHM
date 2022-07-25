# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for idx in range(len(numbers)):
        for second in range(idx+1, len(numbers)):
            answer.append((numbers[idx] + numbers[second]))
    return sorted(list(set(answer)))
    




print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

