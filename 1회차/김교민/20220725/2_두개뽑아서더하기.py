# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer: # answer 안에 numbers[i] + numbers[j]의 값이 있는지 확인
                answer.append(numbers[i] + numbers[j]) #값이 없으면 추가해 주고 있으면 무시해준다.
            
    answer.sort() # answer값을 정렬한다.
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))