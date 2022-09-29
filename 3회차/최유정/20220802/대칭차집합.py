# https://www.acmicpc.net/problem/1269

# lenA, lenB = map(int, input().split())
# A = set(map(int,input().split()))
# B = set(map(int,input().split()))

# print(len(A-B)+len(B-A))

lenA, lenB = map(int, input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
cnt = 0

for a in A:
    if a in B:
        cnt+=1 #중복값 개수
print(lenA + lenB- cnt * 2)

