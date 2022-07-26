# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(1 +i, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = sorted(list(set(answer)))
    # 반복은 시간을 꽤 잡아 먹는 작업. 반복문 밖에서 실행 가능하면 밖에 위치 해줄것
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
