# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    # 모든 요소를 더하기 위한 반복문
    for i in range(len(numbers)): 
        for j in range(i + 1, len(numbers)): #첫번째 요소와 그 다음요소를 더하기 위한 반복문
            if numbers[i] + numbers[j] not in answer: #첫번재 요소와 그 다음 요소가 없으면 answer에 추가
                answer.append(numbers[i] + numbers[j])
    
    #answer = list(answer) not in 했으니 set으로 중복 제거 하지 않아도 됨!
    answer.sort() #결과값 순서대로 정렬하기

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
