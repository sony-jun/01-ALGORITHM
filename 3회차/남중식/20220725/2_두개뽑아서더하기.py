# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    
    # 첫번째 for문, 두 수 중 첫번째 수를 뽑는 for문
    for i in range(len(numbers)):
        # 두번째 수를 뽑는 for문, 첫번째 수 바로 다음 수부터 마지막까지의 수
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    answer = list(set(answer))
    answer.sort()
    
    return answer

from itertools import combinations

def solution2(numbers):

    answer = []
    
    # 조합, numbers 배열 중 2개를 뽑음
    cb = combinations(numbers, 2)
    
    # 그 조합 수들의 합을 answer에 넣음
    for c in cb:
        answer.append(sum(c))
    
    answer = list(set(answer))
    answer.sort()
    
    return answer


print(solution2([2, 1, 3, 4, 1]))
print(solution2([5, 0, 2, 7]))

# 정수 배열 numbers
# 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 수
# 이 수들의 오름차순 정렬 배열
