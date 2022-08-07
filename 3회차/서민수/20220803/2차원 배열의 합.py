list_ = [[1,2,4],
        [8, 16, 3]]

i, j, x, y = 1,1,2,2

i -= 1
j -= 1
x -= 1
y -= 1
sum_ = 0
for r in range(i, x+1):
    for c in range(j,y+1):
        sum_ += list_[r][c]

print(sum_)