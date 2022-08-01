T = int(input())
for i in range(T):
    a = input()
    b = list(a)
    sum = 0

    for i in b:
        if i == '(': # 여는 괄호가 나오면 1을 더해준다.
            sum += 1
        elif i == ')': # 닫는 괄호가 나오면 1을 빼준다.
            sum -= 1
        if sum < 0: # -1이 되면 NO를 출력, for문을 빠져나온다.
            print('NO')
            break

    if sum > 0: # 합이 0보다 크면 NO를 출력
        print('NO')
    elif sum == 0: # 합이 0이라면 YES를 출력
        print('YES')


T = int(input())
for _ in range(1,T+1) :
    w = input()
    
    # '()'가 한쌍 인 것이 VPS => 주어진 괄호를 ()로 묶어서 계속 공백으로 지워나갈 때
   
    # '()'가 계속 한쌍식 성립하여 다 지워진 후 공백만 남는다면 VPS라고 볼 수 있음.
    
    while '()' in w : # w에 '()' 있으면 반복
        w = w.replace('()','') # '()'를 ''로 바꾼다
    if w == '': # ''가 w안에 있으면
        print('YES') # YES
    else :
        print('NO') # 없으면 NO