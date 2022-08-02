T = int(input())

for i in range(T):
    a = input()
    a = list(a)
    cnt = 0
    for j in a:
        if j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt == 0:
        print('YES')
    elif cnt > 0 :
        print('NO')
