#아예 못 풀었음 -> 구글링 식 이해도 못 함,,,

list_= [[1,2,4][8,16,32]]
sum_ = 0
i, j, x, y = 1, 1, 2, 2

i -= 1
j -= 1
x -= 1
y -= 1

for r in range(i, x+1):
    #j -> y
    for c in range(j, y+1):
        sum_ += list_[r][c]

print(sum_)

