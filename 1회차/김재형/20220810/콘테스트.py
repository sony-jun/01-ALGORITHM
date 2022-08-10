import sys
sys.stdin = open('콘테스트_input.txt')

w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]

big_w = []

for a in range(3):
    big_w.append(max(w))
    w.remove(max(w))
big_k = []
for b in range(3):
    big_k.append(max(k))
    k.remove(max(k))
print(sum(big_w), sum(big_k))