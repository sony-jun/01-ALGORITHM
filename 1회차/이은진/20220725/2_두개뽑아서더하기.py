# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    # 순회를 리스트의 인덱스로 하도록 접근
    # 조건문에 인덱스가 겹치지 않으며 answer 리스트에 값이 없을 때
    # 값을 추가하도록 하였다
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (i != j) and (numbers[i] + numbers[j] not in answer):
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
