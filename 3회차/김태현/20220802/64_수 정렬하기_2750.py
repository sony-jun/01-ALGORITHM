import sys
sys.stdin = open("64_수 정렬하기_2750.txt", "r")

N = int(input())

num = []

for i in range(N):
    num.append(int(input()))

num.sort()

for j in num:
    print(j)