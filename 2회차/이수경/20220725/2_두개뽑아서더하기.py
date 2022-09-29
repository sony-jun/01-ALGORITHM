# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []         # 2+1, 2+3, 2+4, 1+3 ... 결과값을 넣을 컨테이너 생성

    for i in range(len(numbers)):      # len(numbers) = 5 ... range(len(numbers)) = 0, 1, 2, 3, 4
        for j in range(i+1, len(numbers)):      # numbers 에서 i번째, 그리고 i+1(=j)번째 요소의 합을 구해야하므로 i, j 에 대한 이중 for문을 작성
            if numbers[i] + numbers[j] not in answer:       # i번째, i+1(=j)번째 요소의 합이 answer에 없었다면
                answer.append(numbers[i] + numbers[j])      # 리스트 형태의 answer 에 새로운 요소로 붙여주기
    answer.sort()    # 리스트 형태의 answer 요소들을 오름차순으로 정렬
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
