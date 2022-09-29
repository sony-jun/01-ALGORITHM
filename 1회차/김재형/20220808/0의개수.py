import sys
sys.stdin = open('0의개수_input.txt')

T = int(input())

# 반복문
for t in range(T):
    n, m = map(int, input().split())
    cnt = 0
    for num in range(n, m+1):
        num_ = str(num)
        if '0' in num_:
            cnt += num_.count('0')
    print(cnt)