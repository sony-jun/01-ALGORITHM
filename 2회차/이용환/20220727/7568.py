T = int(input())
result = []
for i in range(T):
    a = list(map(int, input().split()))
    result.append(a)
for j in result:
    cnt = 1
    for k in result:
        if result.index(j) != result.index(k):
            if j[0] < k[0] and j[1] < k[1]:
                cnt += 1
    print(cnt, end= ' ')