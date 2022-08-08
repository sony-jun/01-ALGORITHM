classes = int(input())
for i in range(1, classes + 1):
    line = list(map(int, input().split()))
    points = line[1::]
    points = sorted(points)
    gap = 0
    for j in range(len(points) - 1):
        if points[j + 1] - points[j] > gap:
            gap = points[j + 1] - points[j]

    print(f'Class {i}')
    print(f'Max {points[-1]}, Min {points[0]}, Largest gap {gap}')