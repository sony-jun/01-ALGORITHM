# 괄호
N=int(input())

for _ in range(N):
    cnt = 0
    list_ = list(input())
    for i in range(len(list_)):
        if list_[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")