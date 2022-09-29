
A,B = map(int,input().split())

while A % B != 0:
    A=int(A//B)
    B=int(A%B)

print(A // B)
