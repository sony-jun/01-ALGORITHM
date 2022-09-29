import sys

sys.stdin = open("70_유니크.txt")

n = int(input())


list_ =  [list(map(int, input().split())) for _ in range(n)]
for tc in range(n):
    
    s = 0
    for j in range(3):
        t = list_[tc][j]
        ok = 1
        for k in range(n):
            if k == tc:
                continue
            if list_[k][j] == t:
                ok = 0; break
        if ok == 1:
            s += t
    print(s)
        