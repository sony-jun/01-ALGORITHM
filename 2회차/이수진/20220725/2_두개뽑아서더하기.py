# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    temp = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] != numbers[j] :
                temp.append(numbers[i]+numbers[j])
    answer = set(sorted(temp))
    
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
