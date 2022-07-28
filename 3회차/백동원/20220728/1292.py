# 쉽게 푸는 문제

A, B = map(int, input().split())
number = 1
number_list = []
if A == 1 and B == 1:
    print(1)
else:    
    while number <= B:                  # 꼭 모든 수열을 생성할 필요 없이 B번째까지만 생성한다.
        for _ in range(number):         # number를 number만큼 생성하기 위한 반복문
            number_list.append(number)
        number += 1
    answer = sum(number_list[A-1 : B])  # 필요한 구간을 인덱스로 추출하여 sum 
    print(answer) 