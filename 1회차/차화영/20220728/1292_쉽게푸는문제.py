import sys
sys.stdin = open("1292.txt")

s = []
a, b = map(int, input().split())
for i in range(1000): # 1 ≤ A ≤ B ≤ 1,000이므로
    for _ in range(i):
        s.append(i)
print(sum(list(s)[a-1:b]))