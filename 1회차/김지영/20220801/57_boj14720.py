# 딸기, 초코, 바나나
# 첫재줄 우유 가게 수 N
# 0 : 딸기, 1 : 초코, 2: 바나나
# n = 12
# m = [0, 1, 2, 0, 0, 1, 2, 1, 2, 1, 0, 1]
n = int(input())
m = list(map(int,input().split()))

stack = []
i = 0
while len(m) != 0:
    # 시작할때 stack에 아무것도 없으면 index range error
    if stack == [] and m[0] == 0:
        stack.append(m[0])
        del m[0]    
    if i % 3 == 0:
        if stack[i] == 0 and m[0] == 1: 
            i += 1
            stack.append(m[0]) 
            del m[0]
        else : 
            del m[0] 
    elif i % 3 == 1:
        if stack[i] == 1 and m[0] == 2:
            i += 1
            stack.append(m[0])
            del m[0]
        else : 
            del m[0] 
    elif i % 3 == 2:
        if stack[i] == 2 and m[0] == 0:
            i += 1
            stack.append(m[0])
            del m[0]
        else : 
            del m[0] 
    print('m:',m,'stack:',stack,i)
print(len(stack))
