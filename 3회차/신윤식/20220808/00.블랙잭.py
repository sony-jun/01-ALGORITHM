N, M = map(int,input().split())
lst = list(map(int,input().split()))
sum_score = 0

for i in range(N-3+1):
    for j in range(i+1, N-3+2):
        for k in range(j+1, N):
            if lst[i] + lst[j] + lst[k] <= M:
                if sum_score < lst[i] + lst[j] + lst[k]:
                    sum_score = lst[i] + lst[j] + lst[k]

print(sum_score)