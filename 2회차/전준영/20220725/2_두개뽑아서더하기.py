# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    temp=[]
    temp0=[]
    for i in numbers:
        for k in temp:
            temp0.append(k+i)
        temp.append(i)
    some=set((temp0))
    answer=list(some)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
