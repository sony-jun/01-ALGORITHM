import sys
sys.stdin = open('B2669.txt')
#평면 위 모든 x좌표와 y좌표는 1이상이고 100이하인 정수
plain = [[0]*101 for _ in range(101)] #칸마다 0인 101*101짜리 matrix 만들어서 
for _ in range(4): # 직사각형 4개
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            plain[i][j] = 1 # 직사각형 겹치는 부분만 1로 만들고 그거 합계 구하기
print(sum(sum(plain, [])))
    