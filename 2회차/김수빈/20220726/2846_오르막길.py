N = int(input())
road = list(map(int, input().split()))
total = 0
upp = []

for i in range(0, N - 2):
    if road[i] < road[i + 1]:
        total += road[i + 1] - road[i]
        if i == N - 1:
            upp.append(total)
    else:
        upp.append(total)
        total = 0

print(max(upp))