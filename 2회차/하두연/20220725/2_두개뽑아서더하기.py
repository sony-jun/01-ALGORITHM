# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    for e in range(0,len(numbers)):
        for i in range(e+1,len(numbers)):
            answer.append(numbers[e] + numbers[i])
        answer = list(set(answer))
        answer.sort()

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

# 이 문제는 구글링
 
