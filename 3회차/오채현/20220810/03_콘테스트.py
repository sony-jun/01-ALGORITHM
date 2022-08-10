total = []
# total = list(range(20))
for _ in range(20):
    total.append(int(input()))

w = total[0:10]
k = total[10::]

w.sort(reverse=True)
k.sort(reverse=True)

print(sum(w[0:3]), sum(k[0:3]))
