def pair(s):
    stack = []
    dic = {'(':')','[':']'}
    result = 'yes'
    for c in s:
        if c in '([':
            stack.append(c)
        elif c in ')]':
            if stack == []:
                result = 'no'
                break
            elif c == dic[stack[-1]] :
                stack.pop()
            else:
                result = 'no'
                break
    if len(stack) != 0:
        result = 'no'
    return result
ln = []
while True:
    s = input()
    if s == '.':
        break
    ln.append(s)
# print(ln)
for s in ln:
    print(pair(s))