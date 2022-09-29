ret = []

for _ in range(5):
    ret.append(int(input()))

print(sum(ret) // 5, sorted(ret)[5 // 2], sep='\n')