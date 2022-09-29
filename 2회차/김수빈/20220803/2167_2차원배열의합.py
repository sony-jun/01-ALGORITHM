N, M = map(int, input().split())
list_ = []
list_2 = []

for _ in range(N):
    list_.append(list(map(int, input().split())))

K = int(input())

for _ in range(K):
    list_2.append(list(map(int, input().split())))

a = min(list_2[0], list_2[2])
b = max(list_2[1], list_2[3])

for _ in range(b):


## 풀이
list =
i, j, x, y =
i -= 1
j -= 1
x -= 1
y -= 1

sum_ = 0
for r in range(i, x+1):
    for c in range(j, y+1):
        sum_ += list_[r][c]
print(sum_)