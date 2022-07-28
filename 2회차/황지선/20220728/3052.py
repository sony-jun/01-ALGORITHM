# 3052번 나머지

n= []

for i in range(10):
    a= int(input())
    b= a % 42
    n.append(b)

x= set(n)
print(len(x))