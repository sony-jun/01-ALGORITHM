# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    # numbers의 길이만큼 순회
    for i in range(len(numbers)):
        # i의 다음 수부터 numbers의 길이만큼 순회
        for j in range(i+1, len(numbers)):
            # answer 리스트에 i 인덱스의 값과 j 인덱스의 값을 더해서 추가
            answer.append(numbers[i] + numbers[j])

    # answer 리스트에서 중복을 제거하기 위해 set함수 사용
    answer = set(answer)
    # 답을 리스트로 반환하기 위해 list함수 사용
    answer = list(answer)
    # 답을 오름차순으로 나타내기 위해 sort() 함수 사용
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
