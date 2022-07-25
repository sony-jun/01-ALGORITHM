# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 문제.두 개 뽑아서 더하기



# 함수의 인자
'''
1. numbers 리스트 자료형
- 2 <= numbers 길이 <= 100
- 0 <= numbers 수 <= 100
'''



# 함수의 반환값
'''
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환
'''



# 코드
def solution(numbers):
    # 중복제거를 위해 값을 set 자료형에 저장
    answer = set()
    # 첫번째 값 선택(numbers 인자를 0부터 -2 인덱스까지 순차적으로 접근)
    for i in range(0, len(numbers) - 1):
        # 두번째 값 선택(numbers인자를 첫번째 값 이후부터 마지막 인덱스까지 순차적으로 접근)
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])   # 선택한 두 값을 더해서 answer 변수에 값 추가
  
    return sorted(answer)   # 정렬한 후 값 반환


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))