T = int(input())

for test_case in range(T):
    number = []
    total = {}

    for a in range(2):
        M = int(input())
        qna =list(map(int,input().split()))
        number += qna
    
    for a in number :
        total[a] = total.get(a,0) + 1
    
    
    for a in number[M:] :
        if total[a] >= 2:
            print(1)
        else:
            print(0)