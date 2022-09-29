# n = int(input())
n = 8
cnt_dict = {}
# cnt_list = [0 for _ in range(n)]

cnt = 0
for _ in range(n):
    c, m = map(int, input().split())
    if c not in cnt_dict:
        cnt_dict[c] = m
    elif c in cnt_dict and cnt_dict[c] != m:
        cnt += 1
        cnt_dict[c] = m
print(cnt)
