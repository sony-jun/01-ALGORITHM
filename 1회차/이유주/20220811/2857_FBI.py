#FBI 요원을 찾는 프로그램 작성
import sys
sys.stdin = open("input.txt")

name = [input() for _ in range(5)]

count = 0
for i in range(5):
    if "FBI" in name[i]:
        print(i+1, end=' ')
        count += 1


if count == 0:
    print("HE GOT AWAY!")