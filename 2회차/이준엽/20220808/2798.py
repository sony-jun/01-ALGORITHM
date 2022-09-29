n,m = map(int,input().split())
numbers = list(map(int,input().split()))
ms_sum = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            s_sum = numbers[i]+numbers[j]+numbers[k]
            if 0<=ms_sum<s_sum and s_sum<=m:
                ms_sum = s_sum
print(ms_sum)