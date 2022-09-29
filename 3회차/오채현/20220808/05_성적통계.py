K = int(input())

for k in range(1, K+1):
    kclass = list(map(int, input().split()))
    scores = kclass[1::]
    rank = sorted(scores)
    gap = 0
    n = kclass[0]
    for i in range(n - 1):
        if rank[i+1] - rank[i] > gap:
            gap = rank[i+1] - rank[i]

    print(f'Class {k}')
    print(f'Max {max(scores)}, Min {min(scores)}, Largest gap {gap}')
