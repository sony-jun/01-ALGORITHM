# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j: # numbers의 인덱스가 다른 경우에만 덧셈 진행
                answer.append(numbers[i] + numbers[j])
    answer = set(answer)
    return sorted(list(answer))


# print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))