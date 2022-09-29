N, M = map(int, input().split())
num_list = list(map(int, input().split()))
max_total = 0
for a in range(N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            total = num_list[a] + num_list[b] +num_list[c]
        
            if max_total < total <= M:
                max_total = total

print(max_total)

