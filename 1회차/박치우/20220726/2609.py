a, b = map(int,input().split())
mul = 1
if a > b :
    big = a
elif b > a :
    big = b
A = a
B = b
lst = []
for i in range(2,big+1):
    if A % i == 0 and B % i == 0:
        A = A / i
        B = B / i
        lst.append(i)
        if A % i == 0 and B % i == 0:
            A = A / i
            B = B / i
            lst.append(i)
for j in range(len(lst)):
    mul *= lst[j]
print(mul)
a = a // mul
b = b // mul
print(a * b * mul)

    









