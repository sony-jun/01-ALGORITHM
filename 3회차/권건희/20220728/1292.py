a,b=map(int,input().split())
cnt=[]
sum=0

for i in range(1,b+1):
  for j in range(i):
    cnt.append(i)

for i in range(a, b+1):
  sum+=cnt[i-1]
print(sum)