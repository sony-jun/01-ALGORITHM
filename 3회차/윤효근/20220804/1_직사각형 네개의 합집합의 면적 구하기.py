import sys

sys.stdin = open("1_직사각형 네개의 합집합의 면적 구하기.txt")

cor = [[0] * 100 for _ in range(100)]
#x,y가 100까지므로 100*100 배열을 0으로 초기화
result = 0


for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            cor[i][j] = 1
    #주어진 사각형의 면적만큼 1로 변경

for r in cor:
    result += sum(r)
#각 행의 총합을 저장

# for i in cor :
#     for j in i:
#         print(j,end=" ")
#     print()

print(result)