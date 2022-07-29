a = list(map(int,input().split()))
b = list(map(int,input().split()))
scoreA = 0
scoreB = 0
 
for i in range(10):
    A = a[i]
    B = b[i]
    if A > B:
        scoreA += 3
    if B > A:
        scoreB += 3
    else : 
        scoreA += 1
        scoreB += 1
if scoreA > scoreB:
    print(scoreA,scoreB)
    print('A')
elif scoreA < scoreB:
    print(scoreA,scoreB)
    print('B')
else : 
    print(scoreA,scoreB)
    print('D')