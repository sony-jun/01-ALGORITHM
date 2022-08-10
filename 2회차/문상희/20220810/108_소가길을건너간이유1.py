cnt = 0
check = {}
n = int(input())
for i in range(n):
    num, pos = map(int, input().split())
    if num in check:
        if check[num] != pos:
            cnt += 1
            check[num] = pos
    else:
        check[num] = pos
print(cnt)