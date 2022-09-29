n,m = map(int,input().split())
card = list(map(int,input().split()))
mx = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            total = card[i] + card[j] + card[k]
            if mx < total <= m: # max 값 갱신
                mx = total
            if total == m:
                mx = total
                break # 의미 있나..?
print(mx)