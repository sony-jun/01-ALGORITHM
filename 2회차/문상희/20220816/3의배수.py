# BOJ - 1769

num = str(input())
cnt = 0
while len(num) > 1:
    num = list(num)
    result = 0
    for i in num:
        result += int(i)
    num = str(result)
    cnt += 1
print(cnt)
if int(num) % 3 == 0:
    print('YES')
else:
    print('NO')