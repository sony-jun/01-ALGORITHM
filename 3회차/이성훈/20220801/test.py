N = int(input())

for i in range(N):
    T = input()
    list_ = []

    for i in T:
        if i == '(':
            list_.append(i)
        elif i == ')':
            if len(list_) != 0:
                list_.pop()
            else:
                print('NO')
                break

    else:
        if len(list_) == 0:
            print('YES')
        else:
            print('NO')

