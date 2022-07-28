# https://school.programmers.co.kr/learn/courses/30/lessons/68644



def solution(numbers):
    answer = []
    sum = 0
    # for문 두갠데 서로 다른 인덱스라고 했으니까 len으로 for문 두개, set
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            sum = numbers[i] + numbers[j]
            answer.append(sum)
            answer = list(set(answer))
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))




































# def solution(numbers):
#     answer = []
#     sum = 0
    
#     for i in range(0, len(numbers)):
#         for j in range (i+1, len(numbers)):
#             sum = int(numbers[i]) + int(numbers[j])
#             answer.append(sum)
#     answer = list(set(answer))
#     answer.sort()
    
#     return answer

# print(solution([2, 1, 3, 4, 1]))
# print(solution([5, 0, 2, 7]))