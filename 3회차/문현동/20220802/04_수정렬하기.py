import sys
sys.stdin = open("04_수정렬하기.txt", 'r')

arr = []

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    
    arr.append(num)

arr.sort()

for i in arr:
    print(i)