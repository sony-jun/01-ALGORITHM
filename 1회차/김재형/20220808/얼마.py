import sys
sys.stdin = open('얼마_input.txt')

T = int(input())


for _ in range(T):
    car = int(input())
    option = int(input())
    for i in range(option):
        op, price = map(int, input().split())
        car += op * price
    print(car)