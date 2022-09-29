# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = set()     # 계속 중복값이 나오길래 처음부터 중복제거를 설정하고 시작.
    for i in range(len(numbers)):   # numbers길이만큼 범위설정
        for x in range(i+1,len(numbers)):     # 1~ numbers길이-1 까지 
            if numbers[i] + numbers[x] != answer: # 변수 i자리의 요소 + 변수 x자리의 요소가 answer안에 없다면
                answer.add(numbers[i]+ numbers[x]) # 변수 i자리의 요소 + 변수 x자리의 요소 를 answer안에 더해라.
    answer = list(answer) #정렬을 하기 위해 list로 변환
    answer.sort() #리스트정렬
    return answer # 함수리턴하여 출력


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
