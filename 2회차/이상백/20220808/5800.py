T = int(input())
for i in range(1, T+1):
    K = list(map(int, input().split()))
    Y = K.sort(reverse= True)

    gaps = []

    for j in (K - 1):
        gap = K[j] - K[j + 1]
        gaps.append(gap)

        largest_gap = max(gaps)

    print(f'Class {i}')
    print(f'Max {max(K)}, Min {min(K)}, Largest gap {largest_gap}')