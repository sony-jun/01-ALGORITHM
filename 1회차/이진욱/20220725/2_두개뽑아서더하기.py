# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            sum = numbers[i] + numbers[j] # 이중반복문을 통해 두 수의 합을 구한다.
            answer.append(sum)

    answer = list(set(answer)) # 중복을 제거한다.

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
