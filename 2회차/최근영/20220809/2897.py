r,c = list(map(int,input().split()))
matrix = [list(map(str,input())) for _ in range(4)]

zero_cnt=0
one_cnt=0
two_cnt=0
three_cnt=0
four_cnt=0
dx = [1, 0 ,1]
dy = [0, 1, 1]


for i in range(r-1):
    for j in range(c-1):
        if matrix[i][j] == '#':
            continue
        elif matrix[i][j] == 'X':
            X_cnt = 0
            cnt = 0
            for l in range(len(dx)):
                ni = i + dx[l]
                nj = i + dy[l]
                if matrix[ni][nj] == '#':
                    X_cnt = 0
                    cnt = 0
                    break
                elif matrix[ni][nj] == 'X':
                    X_cnt += 1
                elif matrix[ni][nj] == '.':
                    cnt +=1
            if X_cnt == 0 and cnt == 3:
                one_cnt += 1
            elif X_cnt == 1 and cnt ==2:
                two_cnt += 1
            elif X_cnt == 2 and cnt ==1:
                three_cnt += 1
            elif X_cnt == 3 and cnt == 0:
                four_cnt += 1
        elif matrix[i][j] == '.':
            X_cnt = 0
            cnt = 0
            for k in range(len(dx)):
                ni = i + dx[k]
                nj = i + dy[k]
                if matrix[ni][nj] == '#':
                    X_cnt = 0
                    cnt = 0
                    break
                elif matrix[ni][nj] == 'X':
                    X_cnt += 1
                elif matrix[ni][nj] == '.':
                    cnt +=1
            if X_cnt == 0 and cnt == 3:
                zero_cnt += 1
            elif X_cnt == 1 and cnt ==2:
                one_cnt += 1
            elif X_cnt == 2 and cnt ==1:
                two_cnt += 1
            elif X_cnt == 3 and cnt == 0:
                three_cnt += 1

print(zero_cnt)
print(one_cnt)
print(two_cnt)
print(three_cnt)
print(four_cnt)