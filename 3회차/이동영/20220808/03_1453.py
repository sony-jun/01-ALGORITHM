pc = list(range(1,101))

n = int(input())
cnt = 0
list_ = []

list_= list(map(int, input().split()))

for i in list_:    
    if pc[i-1] != 'X':
        pc[i-1] = 'X'
    else:
        cnt += 1

print(cnt)