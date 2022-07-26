# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    for i in numbers:
        for j in numbers:
            if numbers.index(i) != numbers.index(j) :
                answer.append(i+j)
        
    answer = list(set(answer))
    return answer

# i 나 j에 숫자만 들어가니까 자꾸 1이 인덱스 2의 1만 나옴


# def solution(numbers):
#     answer = set()
#     for i in range(len(numbers)) :
#         for j in range(i+1, len(numbers)):
#             answer.add(numbers[i]+numbers[j])
            
#     answer = sorted(list(answer))
#     return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
