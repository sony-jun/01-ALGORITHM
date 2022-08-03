a, b = map(int,input().split())
result=[]
for i in range(1,min(a,b)+1):
    if a%i == 0 and b%i == 0:
        result.append(i)
gcd = max(result)
lcd = (a//gcd)*(b//gcd)*gcd
print(gcd)
print(lcd)