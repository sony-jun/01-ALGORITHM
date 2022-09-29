import sys
sys.stdin = open("3_영화감독숌.txt")

num = int(input())
cnt = 0
x = 665

while cnt != num:
    x += 1
    if str(x).count('666'):
        cnt += 1

print(x)