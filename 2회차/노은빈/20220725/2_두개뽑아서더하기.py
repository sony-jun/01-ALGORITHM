# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[j] + numbers[i]  #numbers의 인덱스 값끼리 임의로 뽑아 더하기
            answer.append(result)  #리스트에 result 값 추가

    same = set(answer)   #중복 제거
    answer = list(same)  #중복 제거한 값을 리스트로
    answer.sort()        #정렬

    return answer   


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
