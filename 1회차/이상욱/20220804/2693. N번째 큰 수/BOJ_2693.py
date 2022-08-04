import sys
sys.stdin = open('2693.txt')

N = 3
T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[-N])