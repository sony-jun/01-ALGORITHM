list_= [[1, 2, 4],
        [8, 16, 24]]
i, j, x, y = 1, 1, 2, 2

# i, j, x, y에서 1씩 빼서 인덱스화
i -= 1
j -= 1
x -= 1
y -= 1

sum = 0 
# 이중 반복문
# i -> x
for r in range(i, x+1):
    # j -> y:
    for c in range(j, y+1):
        sum += list_[r][c]
print(sum)