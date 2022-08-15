# 암호문-1


for i in range(10):
    N = int(input())
    Num = input().split()
    T = int(input())
    li = input()
    for i in li:
        if li[i] == 'I':
            x = li[i+1]
            y = li[i+2]
            for idx in y:
                s = li[i+3+idx]
                Num.insert(s)

#망...ㅠㅠㅠ