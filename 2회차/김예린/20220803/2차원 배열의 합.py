list_ = int

i, j, x, y = 1, 1, 2, 2

i -= 1
j -= 1
x -= 1
y -= 1

sum_ = 0
for r in range(1, x + 1):
    for c in range(j, y+1):
        sum_ += list_[r][c]

