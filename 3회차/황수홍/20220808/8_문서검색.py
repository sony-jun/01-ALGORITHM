a = input()
b = input()
cnt = 0

while 1:
    if b not in a:
        break
    a = a.replace(b,' ',1)
    cnt += 1
print(cnt)