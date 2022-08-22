import sys
sys.stdin = open("51_듣보잡_1764.txt", "r")

N, M = map(int, input().split())

a = set()
for i in range(N):
    a.add(input())

b = set()
for i in range(M):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)