# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 문제설명 : 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []

    set_ = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]

            sum_ = n1 + n2

            set_.add(sum_)

    #순서가 없는 set을 순서가 있는 list로 전환
    list_ = list(set_)
    answer = sorted(list_)

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
