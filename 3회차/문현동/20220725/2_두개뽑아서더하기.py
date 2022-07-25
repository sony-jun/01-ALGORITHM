# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    
    answer = []

    for i in range(len(numbers)):
        numbers_pop = list(numbers)
        ele = numbers_pop.pop(i)
        for j in numbers_pop:
            answer.append(ele + j)

    answer = sorted(list(set(answer)))
    
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

# set 에다가 계속 담은다음에 list.sort 해서 제출