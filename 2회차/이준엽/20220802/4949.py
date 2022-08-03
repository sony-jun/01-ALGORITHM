while True:
    b_judge = input()
    stack = []
    answer = 'yes'
    if b_judge == '.':
        break
    for bra in b_judge:
        if bra == '(' or bra == '[':
            stack.append(bra)
        elif bra == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break
        elif bra == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
    if len(stack) != 0:
        answer = 'no'
    print(answer)


# while True:
#     s = input()
#     stack_ = []
#     result = 'yes'

#     if s == '.':
#         break

#     for i in s:
#         if i == '(' or i == '[':
#             stack_.append(i)
#         elif i == ')':
#             if len(stack_) == 0 or stack_[-1] == '[':
#                 result = 'no'
#                 break
#             elif stack_[-1] == '(':
#                 stack_.pop()
#         elif i == ']':
#             if len(stack_) == 0 or stack_[-1] == '(':
#                 result = 'no'
#                 break
#             elif stack_[-1] == '[':
#                 stack_.pop()

#     if len(stack_):
#         result = 'no'

#     print(result)



while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')