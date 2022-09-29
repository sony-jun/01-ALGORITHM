import sys

sys.stdin = open("3_수 정렬하기.txt")

n= int(input())
result =[]
for _ in range(n):
    tmp=int(input())
    result.append(tmp)
result.sort()
for i in result:
    print(i)