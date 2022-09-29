time = int(input())
h = list(map(int, input().split()))
high = 0
total_list = []
total = 0
for t in range(time):
  # 오르막일때
  if (h[t-1] < h[t]) and (t != 0):
    high = h[t] - h[t-1]
    bigyo = h[t]
    total += high
    total_list.append(total)
# 내리막이거나 평지
  else:
    total_list.append(total)
    high, total, bigyo = 0, 0, h[t]
print(max(total_list))

    