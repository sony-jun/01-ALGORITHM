<<<<<<< HEAD
weight = []
height = []
dungchi = []

for i in range(5) :
  w, h = map(int, input().split())

  weight.append(w)
  height.append(h)

  dungchi.append(weight[i] + height[i])

sort_dungchi = sorted(dungchi, reverse=True)


for r in range(5) :
  for s in range(5) :
    if dungchi[r] == sort_dungchi[s] :
      dungchi[r] = s + 1

print(dungchi)

# 정답 코드
n = int(input())

people = []

for i in range(n) :
    w, h = map(int, input().split())
    people.append((w, h))

for a in people :
    rank = 1

    for n in people :
        if (a[0] != n[0]) & (a[1] != n[1]) :
            if (a[0] < n[0]) & (a[1] < n[1]) :
                rank += 1

    print(rank)
=======
weight = []
height = []
dungchi = []

for i in range(5) :
  w, h = map(int, input().split())

  weight.append(w)
  height.append(h)

  dungchi.append(weight[i] + height[i])

sort_dungchi = sorted(dungchi, reverse=True)


for r in range(5) :
  for s in range(5) :
    if dungchi[r] == sort_dungchi[s] :
      dungchi[r] = s + 1

print(dungchi)

# 정답 코드
n = int(input())

people = []

for i in range(n) :
    w, h = map(int, input().split())
    people.append((w, h))

for a in people :
    rank = 1

    for n in people :
        if (a[0] != n[0]) & (a[1] != n[1]) :
            if (a[0] < n[0]) & (a[1] < n[1]) :
                rank += 1

    print(rank)
>>>>>>> cf1fd333db9d11e8bdec5ec8d43a9de3ddfdc1d9
