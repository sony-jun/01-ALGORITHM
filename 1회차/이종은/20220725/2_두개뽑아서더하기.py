# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 정수배열 numbers가 주어짐 
# numbers에서 서로 다른 인덱스에 있는 두개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 리턴하도록 함수 완성
# 3번 조건임, 값을 써보기
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer))) #반복을 할때마다 정렬을 하면 시간이 소요되기 때문에 반복문 밖에서 하는 것이 좋음
#순서가 없는 set을 순서가 있는 리스트로 형변환해야함 

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
