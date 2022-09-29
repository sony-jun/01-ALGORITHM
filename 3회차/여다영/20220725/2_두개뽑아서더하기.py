# https://school.programmers.co.kr/learn/courses/30/lessons/68644

#집합 자료형 set()
#집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
#set()의 괄호 안에 리스트나 문자열을 입력
#중복을 허용하지 않고 순서가 없다.

#숫자리스트.sort()
#숫자리스트를 오름차순으로 정렬

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    final = list(set(answer))
    final.sort() #새로운 변수 안 둬도 됨.
    return final


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
