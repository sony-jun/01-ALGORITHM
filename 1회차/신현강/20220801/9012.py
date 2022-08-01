N = int(input())
for i in range(N):
    a = input()
    count = 0
    last = 0
    t = 0
    for i in range(len(a)):
        if a[i] == '(':
            count += 1
            last = 1
        else:
            count -= 1
            last = 0
            if count < 0 :
                t = 1
    if (count == 0) and (last == 0) and (t == 0):
        print('YES')
    else:
        print('NO')
        