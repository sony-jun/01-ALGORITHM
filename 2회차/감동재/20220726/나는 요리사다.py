n = []
for i in range(0,5):
    n.append(list(map(int,input().split()))) 


_max = 0
index = 0

tmp = []
cnt = 0

for a in n:
    s = sum(a)
    if s > _max:
        _max = s
        index = cnt


print(index , _max)  