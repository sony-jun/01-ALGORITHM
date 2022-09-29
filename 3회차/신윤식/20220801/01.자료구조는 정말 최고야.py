# 1
N, M = map(int,input().split())
tf = []

for i in range(M):
    n = int(input())
    lst = list(map(int,input().split()))
    for j in range(n-1):
        if lst[j] < lst[j+1]:
            print('No')
            exit(0)
print('Yes')


# 2
N, M = map(int,input().split())
lst = []

for i in range(M):
    lst2 = []
    n = int(input())
    lst2 = list(map(int,input().split()))
    lst.append(lst2)

for j in range(1, N+1):
    for k in range(M):
        if len(lst[k]) >= 1 and lst[k][-1] == j:
            lst[k].pop()
            break
    else:
        print('No')
        break
else:
    print('YES')