N = int(input())
list = list(map(int,input().split()))
a = 0
ans = []
for i in range(N-1):
    if list[i] < list[i+1]:
        a += list[i+1] - list[i]
    else:
        ans.append(a)
        a = 0
ans.append(a)
print(max(ans))