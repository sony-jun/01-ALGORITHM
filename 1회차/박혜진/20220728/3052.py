na = []

for i in range(10) :
  a = int(input())
  b = a % 42
  na.append(b)

print(len(set(na)))