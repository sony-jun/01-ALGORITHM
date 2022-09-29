# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1): #처음부터 마지막 전까지 
        for j in range(i+1, len(numbers)): # i이후부터 마지막까지
            answer.append(numbers[i]+numbers[j]) #더한수 추가
    result = set(answer) #중복제거
    answer = list(result) #리스트화
    answer.sort() #정렬
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
