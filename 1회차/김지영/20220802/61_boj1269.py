A,B = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
# A,B = 3,5
# A = {1,2,4}
# B = {2,3,4,5,6}
A_B = set.difference(A,B)
B_A= set.difference(B,A)
AUB = set.union(A_B,B_A)
print(len(AUB))