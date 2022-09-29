def Rev(x):
    mltp=1
    result=0
    for i in str(x):
        result+=int(i)*mltp
        mltp*=10
    return result

X,Y=map(int, input().split())
print(Rev(Rev(X) + Rev(Y)))





X, Y = map(str, input().split())
tem = str(int(X[::-1]) + int(Y[::-1]))
print(tem[::-1])




def Rev(a):
    b = str(a)
    c = b[::-1]
    d = int(c)
    return d
a, b = map(int, input().split())
print(Rev(Rev(a)+Rev(b)))