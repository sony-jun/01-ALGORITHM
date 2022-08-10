import sys
sys.stdin = open("32_박스.txt")

for _ in range(int(input())):
    x, y  = map(int, input().split())
    box = [list(map(int, input().split())) for i in range(x)]
    cnt = 0
    for i in range(y): # 열
        for j in range(x): # 행
            if box[j][i] == 1:
                for k in range(j, x): # 비교할 index(j)를 기준으로 같은 열에 있는 0의 갯수를 세어주는 범위를 정한다.
                    if box[k][i] == 0:
                        cnt += 1
    print(cnt)
                

