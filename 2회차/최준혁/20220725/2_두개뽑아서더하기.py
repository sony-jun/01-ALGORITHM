# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    for i in range(len(numbers)): # 0, 1, 2, 3, 4
        for j in range(i+1, len(numbers)): # 1, 2, 3, 4, 2, 3, 4, 3, 4, 4
            answer.append(numbers[i] + numbers[j]) # 값들을 더한다
    return sorted(list(set(answer))) # 더한것중 set으로 중복을 제거하고 리스트로 담아 정렬


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
