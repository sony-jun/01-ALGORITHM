W = []
for i in range(10):
    point = int(input())
    W.append(point)
W = sorted(W)

K = []
for i in range(10):
    point = int(input())
    K.append(point)
K = sorted(K)

print(sum(W[-1:-4:-1]), sum(K[-1:-4:-1]))