# https://www.acmicpc.net/problem/1543

document = input()
word = input()
stack_str = ''
cnt = 0

for i in range(len(document)):
    stack_str += document[i]
    
    if  word in stack_str:
        cnt += 1
        stack_str = ''
print(cnt)