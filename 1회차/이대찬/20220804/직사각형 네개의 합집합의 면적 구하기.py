import sys

sys.stdin = open('직사각형 네개의 합집합의 면적 구하기.txt')

matrix = [list([0]*10) for _ in range(10)] #매트릭스 원소 입력

for i in range(4):
    lst = list(map(int,input().split()))
    for r in range(lst[0],lst[2]):
        for c in range(lst[1],lst[3]):
            matrix[r][c] = 1
      
print(sum(map(sum,matrix)))


