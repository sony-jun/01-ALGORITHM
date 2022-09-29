# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        j = i + 1
        while j < len(numbers):
            # 중복 제거
            if (numbers[i] + numbers[j] not in answer):
                answer.append(numbers[i] + numbers[j])
            j += 1
    # 오름차순 정렬
    answer.sort()
    return answer

# 중복제거 방법2
# sorted(list(set(answer)))

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
