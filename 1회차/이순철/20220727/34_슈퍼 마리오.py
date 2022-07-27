import sys

sys.stdin = open("34_슈퍼 마리오.txt")

nu = 0
out = 0

for i in range(10):
    a = int(input())
    if out < 100:
        out = nu + a
        nu += a
    else:
        print(nu)

