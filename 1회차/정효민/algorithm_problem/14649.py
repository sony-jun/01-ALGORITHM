import sys


sys.stdin = open('14649.txt')
t = int(input() )
for tc in range(1 , t + 1):
    result = 0
    y = [] #짝수
    x = [] #홀수
    all_list = list(map(int , input().split()))
    for i in range(len(all_list)):
        if i % 2 == 1:
            y.append(all_list[i])
        else:
            x.append(all_list[i])


    # print(10 - ((sum(y) + sum(x) * 2) % 10)  )
    if 10 - ((sum(y) + sum(x) * 2) % 10) > 9:
        result = 0
    else:
        result = 10 - ((sum(y) + sum(x) * 2) % 10)
    print(f'#{tc} {result}')

        