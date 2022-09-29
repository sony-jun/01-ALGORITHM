a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

sum_AB = set(list(A) + list(B))
for s in sum_AB:
    if (s in A) and (s in B):
        A.remove(s)
        B.remove(s)
print(len(A) + len(B))