W = []
K = []

for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))

K.sort(reverse=True)
W.sort(reverse=True)

print(sum(W[:3]),sum(K[:3]))