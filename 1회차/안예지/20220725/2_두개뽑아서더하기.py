# https://school.programmers.co.kr/learn/courses/30/lessons/68644
"""

# 68644.

정수 배열 numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 
더해서 만들 수 있는 모든 수를
배열에 오름차순으로 담아 return 하도록 solution 함수를 완성
numbers의 길이는 2 이상 100이하
numbers의 모든 수는 0이상 100이하

# 입력

[2, 1, 3, 4, 1]
[5, 0, 2 ,7]

# 출력

[2, 3, 4, 5, 6, 7]
[2, 5, 7, 9, 12]

# 접근

1. 인덱스 하나를 바인딩 걸고,
2. 자신을 제외한 인덱스를 순회해서
3. 합의 값을 저장할 리스트를 생성하여 오름차순하여 출력

"""

def solution(numbers):
    # 합의 값이 저장될 리스트
    answer = []
    for idx in range(len(numbers)):
        # 첫 번째 for 문에서 바인딩 될 값
        for a_idx in range(1, len(numbers) + 1):
            # 바인딩된 인덱스 직후의 인덱스 값을 순회합니다.
            if a_idx == len(numbers):
                break
            # 만약 직후 인덱스가 리스트의 길이와 같아진다면 반복을 종료합니다.
            if idx == a_idx:
                continue
            # 직후 인덱스와 현재 바인딩된 인덱스가 같다면 아래의 코드를 실행하지않고 다음 반복을 실행합니다.
            sum_num = numbers[idx] + numbers[a_idx]
            answer += [sum_num]
    answer = list(set(answer))
    # set함수로 중복 제거를 해 주고,
         
    return sorted(answer)
# 오름차순으로 배열한 리스트를 반환합니다.
    









print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
