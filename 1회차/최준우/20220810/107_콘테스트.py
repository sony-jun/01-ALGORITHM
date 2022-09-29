# https://www.acmicpc.net/problem/5576

W = []
K = []
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))
W = sorted(W, reverse= True)
K = sorted(K, reverse= True)

print(W[0]+W[1]+W[2], K[0]+K[1]+K[2])