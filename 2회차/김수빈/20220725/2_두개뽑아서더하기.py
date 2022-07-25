# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        # 뒤에 있는 숫자들은 이미 더했으므로 i + 1 부터 시작함
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))