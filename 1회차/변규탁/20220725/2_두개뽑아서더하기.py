# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        # 마지막 인덱스에서 오류 날것 같아서 break문 생성.
        if i == len(numbers):
            break
        # 맨 앞의 원소 + 나머지 원소 하나씩 더하는 것을 반복.
        for num in numbers[i+1:]:
            answer.add(numbers[i] + num) 
    
    answer_list = list(answer)
    return answer_list


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
