# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    return answer
      
def solution(numbers):
    answer = list()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if not numbers[i] + numbers[j] in answer:
                answer.append(numbers[i] + numbers[j])
        
    return sorted(answer)

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
