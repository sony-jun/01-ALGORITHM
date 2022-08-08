import sys
sys.stdin = open('B9325.txt')

T = int(input())
for tc in range(T):
    car = int(input())
    opt = int(input())
    for i in range(opt):
        q, p = map(int, input().split())
        car += q * p
    print(car)