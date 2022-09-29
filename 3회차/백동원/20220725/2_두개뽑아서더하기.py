# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    result = []
    
    for i in range(len(numbers)):                   # 문자열의 첫번째 숫자를 꺼내고
        for n in range(i+1, len(numbers)):          # 문자열의 두번째 숫자를 꺼내어
            result.append(numbers[i] + numbers[n])  # 합친 수를 리스트에 추가한다. range(i + 1, len(numbers))를 통하여 중복되는 덧셈이 없게 조정하였다.
    answer = list(set(result))                      # 결과 리스트의 중복을 없애기 위해 set을 씌우고 list로 다시 형변화하였다.
    answer.sort()                                   # 오름차순을 위한 sort() 메소드 사용
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
