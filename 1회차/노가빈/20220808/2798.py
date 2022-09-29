n,m = map(int,input().split(' '))
lst = list(map(int,input().split(' ')))
s = 0
for i in range(n):
    for j in range(n):
        for z in range(n):
            if i == j or i == z or j == z:
                continue
            temp = lst[i] + lst[j] + lst[z]
            # print(lst[i], lst[j], lst[z])
            if temp > s and temp <= m:
                s = temp
print(s)