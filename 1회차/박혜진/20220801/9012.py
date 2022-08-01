# 오답 코드
n = int(input())

for i in range(n) :
  gualho = input()
  gualho_list = list(gualho)
  
  sum = 0
  for g in gualho_list :
    if g == '(' :
      sum += 1
    else :
      sum += 2
  
  if sum % 3 == 0 :
    print('YES')
  
  else :
    print('NO')

# 정답 코드
T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")