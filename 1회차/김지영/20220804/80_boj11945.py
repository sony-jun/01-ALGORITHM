y,x = map(int,input().split())
bub= []
for y in range(y):
    b = input()
    b = b[::-1]
    bub.append(b)
for y in bub:
    print(y,end='\n')