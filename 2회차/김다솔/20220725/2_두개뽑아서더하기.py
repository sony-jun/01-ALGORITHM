# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    n = len(numbers)   
    for i in range(n): 
        for j in range(i + 1, n):                    
            answer.append(numbers[i] + numbers[j]) 
            
    answer = set(answer)    
    return sorted(answer)   

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
