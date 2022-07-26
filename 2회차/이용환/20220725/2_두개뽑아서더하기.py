# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer1 = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            X = numbers[i]+ numbers[j]
            answer1.append(X)
    answer1.sort()
    answer = list(set(answer1))
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
