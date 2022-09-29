# num = [39,
# 40,
# 41,
# 42,
# 43,
# 44,
# 82,
# 83,
# 84,
# 85]

num = []
for i in range(10):
    num.append(int(input()))

rest = []

for i in num:
    rest.append(i % 42)
#print(rest)
rest = list(set(rest))
print(len(rest))
