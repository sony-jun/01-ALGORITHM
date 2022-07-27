# N개로 이루어진 수열 A와 정수x
# print A[i] if A[i] < X

lenA, X = map(int, input().split())
A = list(map(int,input().split()))

# lenA = 10
# X = 5
# A = [1,10,4,9,2,3,8,5,7,6]

for i in range(lenA):
    if A[i] < X:
        print(A[i], end = ' ')