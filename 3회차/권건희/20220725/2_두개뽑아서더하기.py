# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    # 두 수를 각 각 가져온다
    # 다만 같은 수면 안되기 때문에 !=사용

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                answer.append(numbers[i]+numbers[j])
    answer=list(set(answer))
    answer.sort()         
 
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
