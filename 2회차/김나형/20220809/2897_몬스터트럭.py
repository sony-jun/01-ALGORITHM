import sys
sys. stdin = open ("2897_몬스터트럭.txt")

r, c = map(int, sys.stdin.readline().split())
parking = [list(sys.stdin.readline()) for _ in range(r)]

d = [(0, 1), (1, 0), (1, 1)]

p = [0, 0, 0, 0, 0]

for i in range(r):
    for j in range(c):
        while True:
            cnt1 = 0
            cnt2 = 0
            if parking[i][j] == '.':
                cnt1 += 1 # 빈 주차 공간
            if parking[i][j] == 'X':    
                cnt2 += 1 # 주차된 차
            for dr, dc in d:
                nr = i + dr
                nc = j + dc
                    
                if 0 <= nr < r and 0 <= nc < c and '.' == parking[nr][nc]:
                    cnt1 += 1
                if 0 <= nr < r and 0 <= nc < c and 'X' == parking[nr][nc]:
                    cnt2 += 1
            if cnt1 == 4 and cnt2 == 0:
                p[0] += 1
                break
            elif cnt1 == 3 and cnt2 == 1:
                p[1] += 1
                break
            elif cnt1 == 2 and cnt2 == 2:
                p[2] += 1
                break
            elif cnt1 == 1 and cnt2 == 3:
                p[3] += 1
                break
            elif cnt2 == 4:
                p[4] += 1
                break
            else:
                break
print(*p, sep='\n')