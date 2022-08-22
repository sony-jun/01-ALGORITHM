import sys
sys.stdin = open("60_배부른 마라토너_10546.txt", "r")

N = int(input())

dic = {}
for _ in range(N):
    runner = input()
    if dic.get(runner, 0):
        dic[runner] += 1
    else:
        dic[runner] = 1

for _ in range(N-1):
    runner = input()
    dic[runner] -= 1

for k, v in dic.items():
    if v == 1:
        print(k)
