import sys
input = sys.stdin.readline

#100*100의 0으로 된 행렬을 만든다.
mat = [[0]*101 for _ in range(101)]


#직사각형 면적에 해당하는 좌표들을 1로 바꿔준다.
for _ in range(4):
    x1, y1, x2, y2 = (map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            mat[i][j] = 1

print(sum(sum(mat, []))) #리스트의 내부를 전부 더해준다.
#sum(mat)으로 하면 정수와 리스트인 mat과 더한다는 의미이므로
#TypeError충돌이 난다. 따라서 sum함수의 두 번째 인자에 []를 넣어줘야
#2차원 리스트를 합칠 수 있다.