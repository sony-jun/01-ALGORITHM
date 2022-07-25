# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = set() # 중복 제거

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer) # answer를 리스트로 변환
    answer.sort() # 정렬하기 위해 .sort()를 사용

    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))