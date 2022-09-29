C = ['c','d','e','f','g','a','b','C']
C = [i for i in range(1,len(C)+1)]
m = list(map(int,input().split()))
if m == C:
    print('ascending')
elif m == C[::-1]:
    print('descending')
else:print('mixed')