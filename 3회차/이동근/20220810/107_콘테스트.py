import sys

input = sys.stdin.readline

W = []
K = []
for i in range(20):
    if i < 10:
        W.append(int(input()))
    elif i == 10:
        W.sort(reverse=True)
        K.append(int(input()))
    else:
        K.append(int(input()))

K.sort(reverse=True)

print(sum(W[:3]), sum(K[:3]))