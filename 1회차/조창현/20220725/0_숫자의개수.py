# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = input()
b = input()
c = input()
multi = int(a) * int(b) * int(c)

numnum = {}

# 우선 각각 숫자에 맞는 딕셔너리를 0으로 초기화 시켜 만들어 준다.
for i in range(0, 10):
    numnum[str(i)] = 0
# 그리고 다시 숫자를 하나씩 돌면서 키값에 맞는 값들을 1씩 더해준다.
for i in str(multi):
    numnum[i] = numnum.get(i) + 1

for i in range(0, 10):
    print(numnum[str(i)])