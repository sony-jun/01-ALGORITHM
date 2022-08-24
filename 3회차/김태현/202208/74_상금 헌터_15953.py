import sys
sys.stdin = open("74_상금 헌터_15953.txt", "r")

a_mat = [
    [1, 500],
    [2, 300],
    [3, 200],
    [4, 50],
    [5, 30],
    [6, 10]
]

b_mat = [
    [1, 512],
    [2, 256],
    [4, 128],
    [8, 64],
    [16, 32]
]

T = int(input())

for tc in range(T):
    
    a, b = map(int, input().split())
    
    result = 0


    for i in range(len(a_mat)):
        if a > 21 or a == 0:
            break

        a -= a_mat[i][0]
        if a < 0:
            result += a_mat[i][1]
            break
    
    for j in range(len(b_mat)):
        if b > 31 or b == 0:
            break

        b -= b_mat[j][0]
        if b < 0:
            result += b_mat[j][1]
            break

    print(result * 10000)