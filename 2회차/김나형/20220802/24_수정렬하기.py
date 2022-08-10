import sys

sys.stdin = open ("24_수정렬하기.txt")

T = int(input())

li = []

for _ in range(T):
   li.append(int(input())) 

for i in range(len(li)):
    if li:
        print(min(li))
        li.pop(li.index(min(li)))

