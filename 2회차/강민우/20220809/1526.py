N = int(input())

num_list = []
for a in range(N+1):
    cnt = 0
    for b in list(str(a)):
        if b == '7' or b == '4':
            cnt += 1
    
    if cnt == len(list(str(a))):
        num_list.append(a)

print(max(num_list))