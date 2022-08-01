n, m = map(int,input().split())

for _ in range(m):
    f = int(input()) 
    stack = [] 
    p = True
    lst= list(map(int,input().split()))
    for i in range(f) :
        if lst[0] > lst[i+1] :
            stack. append(lst)
#이 이후로 모르겠다...          

# 4 2
# 2
# 3 1
# 2
# 4 2

# 5 2
# 3
# 3 5 1
# 2
# 4 2