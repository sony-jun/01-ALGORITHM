import sys

sys.stdin = open("20_괄호.txt")

T = int(input())

for _ in range(T):
    tc = list(map(str, input()))
    sum_tc = 0     
    for i in tc:
      
        if i == '(': # VPS 여는 괄호가 먼저 들어와야 VPS 성립
            sum_tc += 1
        elif i == ')':
            sum_tc -= 1
        if sum_tc < 0: # 처음부터 -1이 될 경우 ')'가 들어왔기 때문에 VPS가 아니다.
            print('NO')
            break

    if sum_tc > 0:
        print('NO')
    elif sum_tc == 0:
        print('YES')


    
    