def Rev(x):
    a = str(x)[::-1]
    return int(a)

X,Y = map(int,input().split(' '))

print(Rev(Rev(X)+Rev(Y)))
    
 