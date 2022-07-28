a, b = map(int, input().split())

num = []

for i in range(45) :
  for o in range(i) :
    num.append(i)

print(sum(num[a-1:b]))