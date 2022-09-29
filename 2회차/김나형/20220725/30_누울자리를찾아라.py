import sys
sys.stdin = open("30_누울자리를찾아라.txt")

N = int(input())

space = [list(map(str, input())) for _ in range(N)]
bed_r = 0
bed_c = 0
for i in space:
    cnt = 0
    for j in i:
        if j == '.':
            cnt += 1
        else:
            if cnt >= 2:
                bed_r += 1
                break
            cnt = 0
        if cnt == 2:
            bed_r += 1
            break

for c in range(N):
    cnt  = 0
    for r in range(N):
        if space[r][c] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                bed_c += 1
                break
            cnt  = 0
        if cnt == 2:
            bed_c += 1
            break
print(bed_r, bed_c)
