# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for idx in range(len(numbers)-1):
        for sec_num in numbers[idx+1:]:
            if numbers[idx]+sec_num not in answer:
                answer.append(numbers[idx]+sec_num)
    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
