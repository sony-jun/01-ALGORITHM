import sys
sys.stdin = open("86_얼마_9325.txt", "r")

T = int(input())

for tc in range(T):
    car = int(input())
    tool = int(input())
    for i in range(tool):
        a, b = map(int, input().split())
        car += a * b
    print(car)