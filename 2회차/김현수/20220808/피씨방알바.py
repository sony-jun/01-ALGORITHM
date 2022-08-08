# import sys
# sys.stdin = open("피씨방알바.txt")

# N = int(input())
# line = list(map(int,input().split()))

N = 10
line = [10, 2, 1, 10, 2, 5, 7, 9, 65, 8]
cnt = 0
dic_ = dict()

for _ in range(N):
    if line[_] not in dic_:
        dic_[line[_]] = 1
    elif line[_] in dic_ :
        cnt += 1
print(cnt)