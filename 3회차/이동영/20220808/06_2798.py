import itertools

n, m = map(int, input().split())

list_ = list(map(int, input().split()))

comb = list(itertools.combinations(list_ , 3))
temp = []

for i in comb:
    if sum(i) <= m:
        temp.append(sum(i))

print(max(temp))