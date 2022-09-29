from itertools import combinations

nine = []

for _ in range(9) :
    nine.append(int(input()))

seven = list(combinations(nine, 7))

for i in seven :
    if sum(i) == 100 :
        real_seven = sorted(i)

for r in real_seven :
    print(r)