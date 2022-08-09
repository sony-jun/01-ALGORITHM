import itertools

list_ = []
for _ in range(9):
    list_.append(int(input()))

permu = list(itertools.permutations(list_, 7))

for i in permu:
    if sum(i) == 100:
        result = list(i)
        break
result.sort()
for j in result:
    print(j)