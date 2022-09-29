import sys
sys.stdin = open("20220802/1269_대칭차집합.txt")

A_num, B_num = map(int, input().split())    # 집합 A, B의 원소 개수
A = list(map(int, input().split()))         # 집합 A의 모든 원소
B = list(map(int, input().split()))         # 집합 B의 모든 원소

A_B = list(set(A) - set(B))                 # A-B 차집합
B_A = list(set(B) - set(A))                 # B-A 차집합
result = len(A_B) + len(B_A)                # 각 차집합의 원소 개수 합

print(result)                               # 대칭 차집합의 원소 개수