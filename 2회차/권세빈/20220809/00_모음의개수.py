import sys
sys.stdin = open('00.txt','r')

n =''
v = 'aeiouAEIOU'


while n != '#':
    n = input()
    if n == '#':
        break
    cnt = 0
    for i in n:
        if i in v:
            cnt += 1
    print(cnt)