a,b = input().split()

a = int(a[::-1])
b = int(b[::-1])
c = a+b
print(int(str(c)[::-1]))
