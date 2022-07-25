# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        a=i
        while(a<len(numbers)-1):
            a += 1
            if numbers[i]+numbers[a] not in answer:
                answer.append(numbers[i]+numbers[a]) 
    answer.sort()                  
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))





