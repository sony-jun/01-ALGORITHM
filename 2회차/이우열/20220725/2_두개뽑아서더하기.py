# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        # 이중 for문을 사용하여 같은 인덱스가 아닌 수끼리 더해주고
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])  # 배열에 추가한다

    # set로 중복을 없앤 뒤 리스트로 형 변환하여 정렬한다
    answer = sorted(list(set(answer)))

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
