N = int(input())

num = []

for i in range(N):
    x = int(input())
    
    num.append(x)
num.sort()

for i in num:
    print(i)
