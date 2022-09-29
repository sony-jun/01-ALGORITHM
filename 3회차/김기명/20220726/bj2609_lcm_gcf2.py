A, B  = map(int,input().split())
gcf = []
for i in range(1, A + 1):
    if A % i == 0 and B % i == 0:
        gcf.append(i)
print(gcf[-1])

lcm = []
for i in range(1, A + 1):
    for j in range(1, A + 1):
        if A * i == B * j:
            lcm.append(A * i)
print(lcm[0])                      # 줄였는데도 시간초과