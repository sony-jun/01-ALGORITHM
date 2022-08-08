# https://www.acmicpc.net/problem/2309

dwarves = []
for _ in range(9):
    dwarves.append(int(input()))

from itertools import permutations
c_list = list(permutations(dwarves, 7))
result = []

for i in c_list:
    if sum(i) == 100:
        result = sorted(i)
        break
for i in result:
    print(i)