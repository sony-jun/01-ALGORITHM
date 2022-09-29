n = int(input())

ways = list(map(int, input().split()))
hill = 0
hills = []

for i in range(1, n) :
  if ways[i] > ways[i - 1] :
    hill += ways[i] - ways[i - 1]

    if i == (n - 1) :
      hills.append(hill)

  else :
    hills.append(hill)
    hill = 0

print(max(hills))