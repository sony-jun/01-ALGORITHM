k = int(input())
for i in range(k):
    n = list(map(int,input().split(' ')))
    t = n.pop(0)
    n.sort(reverse=True)

    gap = 0
    for j in range(t-1):
        if n[j] - n[j+1] > gap:
            gap = n[j] - n[j+1]


    print(f'Class {i+1}')
    print(f'Max {n[0]}, Min {n[-1]}, Largest gap {gap}')