h = int(input())
t = []
w = []
rank = {}

for i in range(1,h+1):
    tall,weight = input().split()
    t.append(int(tall))
    w.append(int(weight))
# print(t, w)
score = 0
for i in range(h):
    for j in range(h):
        if t[i] > t[j] and w[i] > w[j]:
            print(t[i],t[j],w[i],w[j])
            score += 1
        rank[i] = score+1
        score = 0
print(rank)