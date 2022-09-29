dy = [0,1,1]
dx = [1,0,1]
break_count_list = [0] * 5

r,c = map(int,input().split())
list_ = []
for _ in range(r):
    temp = list(input())
    list_.append(temp)

for y in range(r):
    for x in range(c):
        break_count = 0
        # print(list_[y][x])
        if list_[y][x] == '#':
            continue
        if list_[y][x] == 'X':
            break_count += 1

        for d in range(3):
            ny = y + dy[d]
            nx = x + dx[d]
            if not (-1 < ny < r and -1 < nx < c):
                break
            if list_[ny][nx] == '#':
                break
            if list_[ny][nx] == 'X':
                break_count += 1
        else :
            break_count_list[break_count] += 1
            
print(break_count_list)