# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = set()
 
    for ind in range(len(numbers)): # 0 ~ n-1        
        for ind2 in range(ind+1,len(numbers)):  # 1 ~ n
            answer.add(numbers[ind] + numbers[ind2])
        
    answer = sorted(list(answer))
    
            
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
