N, M = map(int,input().split())
li = list(map(int,input().split()))
ans = []

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if li[i] + li[j] + li[k] <= M:
                ans.append(li[i] + li[j] + li[k])
print(max(ans))