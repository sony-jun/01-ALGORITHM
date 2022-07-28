s,e = map(int,input().split())
n = e
lst = []
for i in range(1,n+1):
    for _ in range(i):
       lst.append(i)
print(lst)
print(sum(lst[s-1:e]))