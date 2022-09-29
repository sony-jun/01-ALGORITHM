import sys

sys.stdin = open("0_대칭_차집합.txt")

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# A_B = list(set(A) - set(B)) # A 차집합 B
# B_A = list(set(B) - set(A)) # B 차집합 A
print(len(A ^ B)) # 대칭 차집합이기 때문에 (A - B) + (B - A)