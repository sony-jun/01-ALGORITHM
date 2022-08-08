import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

#행렬을 만들어주고
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

K = int(input())
for _ in range(K):
    #입력값을 받아주고
    i, j, x, y = map(int, input().split())
    cnt = 0
    #1번째 인덱스가 0번째 인덱스를 돌아줘야한다.
    for a in range(i-1, x):
        for b in range(j-1, y):
            cnt += matrix[a][b]

    print(cnt)

