import sys
sys.stdin = open('1269.txt')

a, b = input().split()
elem_a = set(input().split()) # 집합 a 생성
elem_b = set(input().split()) # 집합 b 생성
ab = elem_a & elem_b # a와 b의 교집합
r_a = elem_a - ab # a - 교집합
r_b = elem_b - ab # b - 교집합
print(len(r_a) + len(r_b)) # 대칭 차집합의 개수