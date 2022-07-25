# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    num_set = set()
    # set을 만들어서 나중에 겹치는 숫자는 빼준다

    for i in range(len(numbers)):
    # i는 리스트 안에 있는 숫자들의 '인덱스'이다
        for j in range(i+1, len(numbers)):
        # j도 리스트 안에 있는 숫자들의 '인덱스'이지만
        # i+1을 하여, 리스트 안에 있는 인덱스를 1씩 더해준다
            num_set.add(numbers[i] + numbers[j])
            # number[i] 와 number[j]는 '인덱스'의 해당 '값'이다
            # .add()를 통해 num_set에 더해진 숫자들을 넣어준다
            answer = list(num_set)
            # set을 list로 변환하기
            answer.sort()
            # sort 함수를 써서 오름차순으로 반환해준다
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

