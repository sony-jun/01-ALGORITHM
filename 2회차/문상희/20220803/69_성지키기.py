n, m = map(int, input().split())

metrix = [list(input()) for _ in range(n)]
cnt_l = 0
cnt_s = 0
for i in range(n):
    if 'X' not in metrix[i]:
        cnt_l += 1

for i in range(m):
    stripe = []
    for j in range(n):
        stripe.append(metrix[j][i])

    if 'X' not in stripe:
        cnt_s += 1

print(max(cnt_l, cnt_s))
# print(metrix)