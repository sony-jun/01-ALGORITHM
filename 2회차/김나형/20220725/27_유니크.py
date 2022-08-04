from re import L
import sys
sys.stdin = open("26_유니크.txt")


T = int(input())
li = [[], [], []]
for _ in range(T):
    a, b, c = map(int, input().split())
    li[0].append(a)
    li[1].append(b)
    li[2].append(c)
for i in range(T):
    sum = 0
    for j in range(3):
        if li[j].count(li[j][i]) > 1:
            sum += 0
        else:
            sum += li[j][i]
    print(sum)
