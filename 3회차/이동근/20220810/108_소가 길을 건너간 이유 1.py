d = {}
count = 0
for _ in range(int(input())):
    no, lo = map(int, input().split())

    if no not in d:
        d[no] = lo
    else:
        if d[no] != lo:
            d[no] = lo
            count += 1

print(count)