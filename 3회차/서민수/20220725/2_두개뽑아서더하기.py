# https://school.programmers.co.kr/learn/courses/30/lessons/68644


# 리스트 안에 있는 각 수들을 더하여 나올 수 있는 모든 수를 도출해라
# 1+1 = 2, 2+1 = 3, 3+1 = 4 등
# 오름차순 배열 sort()
# [2 1 3 4 1], [2, 1, 3, 4, 1]
# 인덱스0가 더할 수 있는 건 1, 2, 3, 4
# 인덱스1가 더할 수 있는건 2, 3, 4
# 인덱스2가 더할 수 있는건 3, 4
# 인섹스3이 더할 수 있는건 4s
# i => 0~4
# j = i+1~4                                                 
def solution(numbers):
    answer = []
    set_lst = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]
            
            sum_lst = n1 + n2
            set_lst.add(sum_lst)
    #순서가 없는 set을 순서가 있는 lst로 형변환
    list_ = list(set_lst)
    answer = sorted(list_)

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
