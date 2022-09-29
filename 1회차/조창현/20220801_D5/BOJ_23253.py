# import sys

# sys.stdin = open("23253input.txt")

stack = [11, 10, 8, 5]

stack_list = [[12, 4, 1], [6, 2], [9, 3, 7], [11, 10, 8, 5]]


comparison = stack.pop()
for stack in stack_list:
    while len(stack) != 0 :
        print(stack[-1], comparison)
        
        if stack [-1] > comparison:
            comparison = stack.pop()
        else:
            answer = 'NO'
            break
    if answer == 'NO'
        break
print(answer)