w = []
k = []

for i in range(0, 10):
    a = int(input())
    w.append(a)
for i in range(0, 10):
    b = int(input())
    k.append(b)

#w,k 내림차순정렬
w.sort(reverse=True)
k.sort(reverse=True)

wsum = 0
ksum = 0
for i in range(3):
    wsum += w[i]
    ksum += k[i]

print(wsum, ksum)