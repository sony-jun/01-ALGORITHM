# s_ = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

x, y = map(int, input().split())
a = []
for i in range(y + 1):
    for j in range(i):
        if len(a) == y:
            break
        a.append(i)
       
        
print(sum(a[x-1:y]))