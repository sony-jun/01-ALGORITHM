# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []                                     # 항목들을 추가해야할 리스트 설정. = answer

    temp = set()                                    # 중복되는 숫자는 없애고자 set설정.

    for i in range(len(numbers) - 1):               # [2, 1, 3, 4, 1] -> len -> 5 -> 5-1 -> range(4)
        for j in range(i + 1, len(numbers)):        # i = [0, 1, 2, 3] -> range(1, 4)/range(2, 4)/range(3, 4)/range(4, 4)
            temp.add(numbers[i] + numbers[j])       # range(1, 4) -> temp.add(number[0] + numbers[1])/temp.add(numbers[0] + numbers[2])..
                                                    # 결국, 리그전같이 덧셈을 하게 됨.
    answer = list(temp)                             # 중복되는 값이 생기기에 set으로 중복 제거 후 list만들고, 
    answer.sort()                                   # sort로 오름차순으로 정렬.

    return answer                                   # answer 반환.


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
