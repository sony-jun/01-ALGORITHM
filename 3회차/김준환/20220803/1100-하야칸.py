matrix = [list(input()) for _ in range(8)]
cnt = 0
for idx1 in range(8):
    for idx2 in range(8):
        if sum(idx1,idx2) % 2 == 0:
            if matrix[idx1][idx2] == 'F':
                cnt += 1
print(cnt)