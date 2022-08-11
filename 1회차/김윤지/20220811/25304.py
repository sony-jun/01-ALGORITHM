
x = int(input())
n = int(input())

for _ in range(n):
    a, b = map(int,input().split())
    #print(a,b)
    x -= a * b #한줄씩 빼서 
if x == 0 : #0이 되면 yes
    print('Yes')
else:
    print('No')
    