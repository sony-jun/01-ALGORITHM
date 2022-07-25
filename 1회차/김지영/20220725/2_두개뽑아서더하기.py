# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 문제 설명
# 정수 배열 numbers가 주어집니다. 
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 
# return 하도록 solution 함수를 완성해주세요.

# test를 위한 numbers 예시 배열
def solution(numbers):
    answer = []
    # 배열의 마지막 인덱스는 len(numbers)-1 
    # ex) if len(numbers) = 3: last_index = 2
    # 서로 다른 인덱스의 두개의 수를 뽑으려면
    # numbers[0] + numbers[1,2,3,4,5]
    # numbers[1] + numbers[2,3,4,5]
    # ...
    # front = numbers[0]부터 시작하는 기준이 되는 수
    # front는 numbers를 numbers[0]부터 numbers[len(numbers)-1]까지 순회한다.
    # add_front는 front의 다음 인덱스부터 배열의 끝까지 순회한다.
    front = 0
    add_front = 1
    for front in range(len(numbers)-1):
        # print(f'f{front}',numbers[front])    # front값 확인
        for add_front in range(front+1,len(numbers)):
            # print(numbers[front],numbers[add_front])
            answer.append(numbers[front]+numbers[add_front])
    # answer = set(answer)    # 중복제거
    # answer = list(answer)
    # answer = sorted(answer)
    answer = sorted(list(set(answer)))
    return answer
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
