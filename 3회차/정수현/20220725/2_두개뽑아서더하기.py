# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):            
    answer = set()                              # 중복 방지를 위해 set 자료형 선택
    for i in range(len(numbers)):               # 2중 반복문을 사용하지 않고 풀 수 있는 방법이 있을 것 같음
        for j in range(i+1, len(numbers)):      # i를 통해 j의 iteration 수가 줄어듦 T(n) = n(n+1)/2
            answer.add(numbers[i]+numbers[j])
    return sorted(answer)

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
