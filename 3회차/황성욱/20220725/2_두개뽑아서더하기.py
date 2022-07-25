# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    length = len(numbers)
    for i in range(length):
        for j in range(1+i,length):
            res = numbers[i]+numbers[j]
            if res not in answer:
                answer.append(numbers[i]+numbers[j])
            


    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
