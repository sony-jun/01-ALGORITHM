# pn = 5
# lst = [(55,185),(58,183),(88,186),(60,175),(46,155)]

pn = int(input())
lst = []
rank = [0]*pn
for i in range(pn):
    w,h = list(map(int,input().split()))
    lst.append((w,h))
for a in range(pn):
    A = lst[a]
    # print(A)
    for b in range(pn):
        B = lst[b]
        if A[0] > B[0] and A[1] > B[1]:
            rank[b] += 1
for rk in rank:
    print(rk+1,end=' ')