N = int(input())
numlist = list(map(int, input().split()))

# pre는 원래 높이를 뜻함
pre = numlist[0]
high = 0
res = 0
for i in numlist:
    if pre < i: # pre보다 크면
        high += i - pre #오름
    
    else: # 아니면
        res = max(res, high) #내림
        high = 0
    pre = i

print(max(high, res))
