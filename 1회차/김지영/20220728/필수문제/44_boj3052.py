n = []
for _ in range(10):
    n.append(int(input()))
# print(n)
l = [i%42 for i in n]
l = set(l)
print(len(l))