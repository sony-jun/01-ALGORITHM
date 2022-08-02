import sys
sys.stdin = open('3.txt', 'r')

# 수의 개수 받기
N = int(input())

# 개수만큼 입력 받기
n = [int(input()) for _ in range(N)]

# 정렬 후 하나씩 프린트
for i in sorted(n):
    print(i)