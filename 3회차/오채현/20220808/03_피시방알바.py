n = int(input())

csm = list(map(int, input().split()))
pcs = [0] * 101
rjc = 0

for c in csm:
    if pcs[c] == 0:
        pcs[c] += 1
    else:
        rjc += 1

print(rjc)
