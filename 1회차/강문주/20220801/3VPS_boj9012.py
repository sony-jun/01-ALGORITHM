case = int(input())
for _ in range(1, case+1):
    stack = [] #여는괄호를 담아둘 스택
    PS = input()
    VPS = True 
    for i in PS:
        if i == '(':
            stack.append('(') #여는 괄호를 스택에 넣는다.
        elif i == ')':
            if stack: 
                stack.pop() # i의 값이 닫는 괄호일 경우 스택의 맨 끝의 값을 가져온다.
            elif not stack: # 스택 안에 내용이 없을 경우
                VPS = False # False로 초기화
                break
    if not stack and VPS: #스택 비어있거나 True인 경우
        print('YES')
    else: # False인 경우
        print('NO')