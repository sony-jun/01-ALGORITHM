import sys
sys.stdin = open("107_콘테스트_5576.txt", "r")

w = []
k = []

for _ in range(10):
    w.append(int(input()))

for _ in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

re1 = sum(w[:3])
re2 = sum(k[:3])

print(re1, re2)