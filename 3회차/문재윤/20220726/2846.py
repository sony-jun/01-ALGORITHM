n = map(int,input().split())
list_ = list(n)
a = 0
c = 0

for i in n:
    if a <= i:
        a = i
        print(a-c)
    else:
        c = i
        continue
        