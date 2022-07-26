import sys

sys.stdin = open("3_input.txt")
cooks = []

for i in range(5):
    cooks.append(sum(map(int, input().split())))
print(cooks.index(max(cooks))+1, max(cooks))