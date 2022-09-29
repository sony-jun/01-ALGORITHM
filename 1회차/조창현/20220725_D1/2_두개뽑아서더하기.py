# https://school.programmers.co.kr/learn/courses/30/lessons/68644
from re import A


def solution(numbers):
    answer = []
    input = {}
    sum_case = []
    input_num = 1
    ## input 값을 딕셔너리에 {들어온 순서 : 값}으로 넣는다.
    for n in numbers:
        input[input_num] = n
        input_num += 1
    #print(input)
    ## input 을 딕셔너리로 받으면서 들어어온 순서를 키로 잡은건 
    ## 자신과 자신을 더한 값을 빼주기 위해
    for i in input.keys():
        for j in input.keys():
            ## 여기에서 같은 들어온 순서가 다른 경우만 더해주면서 걸러낼 수 있다.
            if i != j:
                sum_case.append(input.get(i) + input.get(j))
    #print(sum_case)
    sum_case = list(set(sum_case))
    #print(sum_case)
    sum_case.sort()
    #print(sum_case)

    return sum_case

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
