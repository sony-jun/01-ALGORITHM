ret = []

for i in range(1, 6):
    if "FBI" in input():
        ret.append(i)

if ret:
    print(*ret)
else:
    print("HE GOT AWAY!")