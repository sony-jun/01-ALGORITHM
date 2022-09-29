# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for a in range(len(numbers)):
        i =1
        while a + i != len(numbers) :
         answer.append(numbers[a] + numbers[a+i])
         i += 1
    answer = list(set(answer))
    

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
