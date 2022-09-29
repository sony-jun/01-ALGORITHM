import sys

sys.stdin = open("46_쉽게 푸는 문제.txt")

# math line = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, .....n,n]
# a는 시작하는 숫자 자리 b는 끝나 숫자 자리
a, b = map(int,input().split())

data = []

for i in range(b+1):
    for j in range(i):
        if b == len(data):
            break
        data.append(i)

print(sum(data[a-1:b]))