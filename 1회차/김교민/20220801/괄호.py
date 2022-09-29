# pop과 append활용을 한다.
# 여는 괄호를 리스트안에 넣고 닫는괄호일 경우 리스트의 완성된 괄호를
# 뽑아내는 내용의 반복문을 작성한다.
# 리스트가 비어있을 경우에 True값을 False로 초기화 시킨다.

case = int(input())
for _ in range(1, case+1):
    stack = [] #여는괄호를 담아둘 리스트
    PS = input()
    VPS = True 
    for i in PS:
        if i == '(':
            stack.append('(') #여는 괄호를 리스트에 넣는다.
        elif i == ')':
            if stack: 
                stack.pop() # i의 값이 닫는 괄호일 경우 리스트의 맨 끝의 값을 가져온다.
            elif not stack: # 리스트가 비어있을 경우
                VPS = False # False로 초기화
                break
    if not stack and VPS: #리스트가 비어있거나 True인 경우
        print('YES')
    else: # False인 경우
        print('NO')