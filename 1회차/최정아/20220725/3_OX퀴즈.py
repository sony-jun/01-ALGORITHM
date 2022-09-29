# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

# input 문자열을 정수 타입으로 변환
n = int(input())
# index로 접근해서 각 숫자 순회
for i in range(n):
    x = str(input())
    sum = 0
    cnt = 0
    # for문 안에 for문 생성
    for j in list(x):
        # 0을 만나면 
        if j == 'O':
            # 1 더함
            cnt += 1
            # 그 값을 sum에 담음
            sum += cnt
        else:
            cnt = 0
    print(sum)