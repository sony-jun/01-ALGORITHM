# n = input()

# vps = True
# pstr = '(())())'

# ps_stack = []
# #괄호를 저장할 스택

# for ps in pstr:
#     if ps == '(':
#         ps_stack.append('(')
#         #여는 괄호면 스택에 추가
#     if ps == ')':
#         if ps_stack:
#             ps_stack.pop()
#             #스택에 원소가 있으면 지우기 > 스택에 들어가는 원소는 여는 괄호 뿐이기 때문에
#             #닫힌 괄호가 나올 때마다 지우면 쌍을 맞춰갈 수 있음
#         elif not ps_stack:
#             vps = False
#             #만일 스택에 남아있는 여는 괄호가 없으면 짝을 맞출 수 없으니 false로 변경 후 반복 탈출
#             break

# if not ps_stack and vps:
#     #반복문 종료 후 여는 괄호 스택이 비어있고 vps 값이 변경된 적이 없으면 짝을 모두 맞춘 것 이므로 True
#     print('YES')
# elif ps_stack or not vps:
#     #여는 괄호 스택에 원소가 남아있거나 vps값이 변경된 경우는 짝을 맞추지 못한 경우 이므로 False
#     print('NO')

T = int(input())

for _ in range(T):
    pstr = input()
    vps = True
    ps_stack = []
#괄호를 저장할 스택

    for ps in pstr:
        if ps == '(':
            ps_stack.append('(')
            #여는 괄호면 스택에 추가
        if ps == ')':
            if ps_stack:
                ps_stack.pop()
                #스택에 원소가 있으면 지우기 > 스택에 들어가는 원소는 여는 괄호 뿐이기 때문에
                #닫힌 괄호가 나올 때마다 지우면 쌍을 맞춰갈 수 있음
            elif not ps_stack:
                vps = False
                #만일 스택에 남아있는 여는 괄호가 없으면 짝을 맞출 수 없으니 false로 변경 후 반복 탈출
                break

    if not ps_stack and vps:
        #반복문 종료 후 여는 괄호 스택이 비어있고 vps 값이 변경된 적이 없으면 짝을 모두 맞춘 것 이므로 True
        print('YES')
    elif ps_stack or not vps:
        #여는 괄호 스택에 원소가 남아있거나 vps값이 변경된 경우는 짝을 맞추지 못한 경우 이므로 False
        print('NO')