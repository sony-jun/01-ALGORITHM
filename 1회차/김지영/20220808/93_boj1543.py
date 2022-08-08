s = input()
f_s = input()
c = 0
stack = ''
for st in s:
    stack = stack + st # 스택에 s문자를 하나씩 받아서
    # print(stack)
    if f_s in stack: # f_s랑 같아지면
        c += 1 # count
        # print(c,stack)
        stack = '' # stack reset
print(c)