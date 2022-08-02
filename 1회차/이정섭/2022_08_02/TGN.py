tc = int(input())

for _ in range(tc) :
  r, e, c = map(int, input().split())
# r = revenue without commercial, e = revenue with commercial, c = commercial cost

  if e - c > r :
    print("advertise")
  elif e - c == r :
    print("does not matter")
  else :
    print("do not advertise")