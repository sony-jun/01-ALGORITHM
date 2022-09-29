a, b = map(int, input().split())

tmp = []
for i in range(1, min(a,b) + 1):    # (a, b) = (24, 18) -> range(1, 19)
    if a % i == 0 and b % i == 0:   # 24 % (1~19) 그리고 18 % (1~19) = 0 이라면
        tmp.append(i)               # tmp에 추가해.

print(max(tmp))                      # temp 중에 최대수 -> 최대공약수
print(max(tmp) * (a // max(tmp)) * (b // max(tmp))) # 최대공약수 * a//최대공약수 * b//최대공약수