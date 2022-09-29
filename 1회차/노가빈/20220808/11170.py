t = int(input())
for j in range(t):
    
    n1,n2 = map(int,input().split(' '))
    s = 0
    for i in range(n1,n2+1,1):
        if '0' in str(i):
            s += str(i).count('0')
    print(s)