# https://www.acmicpc.net/problem/3052

import sys

sys.stdin = open("1.txt", "r")

number = []                 # 입력값 담을 리스트
for _ in range(10):         # 수 10개 받기
    n = int(input())
    number.append(n)        # 입력값 리스트에 추가

result = []                 # 나머지들 담을 결과값 리스트
for i in number:            # 입력값을 하나씩 꺼내서 연산할 반복문
    result.append(i % 42)   # 입력값을 42로 나눈 나머지 구하고 결과값 리스트에 추가
result = len(set(result))   # 중복 없애고 개수를 셈
print(result)

# s = set()
# for _ in range(10):
#     s.add(int(input())%42)
# print(len(s))


# l = [int(input())%42 for i in range(10)]
# print(len(set(l)))