n = int(input())

for i in range(n):
    a = input()
    cnt = 0

    for pos in a:
        if pos == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                print('NO')
                break
    else:
        if cnt == 0:
            print('YES')
        else:
            print('NO')

