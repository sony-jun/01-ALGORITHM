# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

num_cnt = [0] * 10  # 0 ~ 9
abc = str(a * b * c)

for num in abc:
    num_cnt[int(num)] += 1

for cnt in num_cnt:
    print(cnt)