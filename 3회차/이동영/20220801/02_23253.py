n, m = list(map(int, input().split()))
list_ = []
a = True

for i in range(1,m+1):
    m1 = int(input())
    list_ = list(map(int, input().split()))
    if list_ != sorted(list_, reverse=True):
        a = False
         
if a:
    print('Yes')
else :
    print('No')