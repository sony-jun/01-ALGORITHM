ftv1 = {1:500,2:300,3:200,4:50,5:30,6:10}
ftv2 = {1:512,2:256,3:128,4:64,5:32}
T = int(input())
for test_case in range(1,T+1):
    a,b = map(int,input().split())
    if a == 1:
        a = 1
    elif a <= 3 and a > 1:
        a = 2
    elif a <= 6 and a > 3:
        a = 3
    elif a <= 10 and a > 6:
        a = 4
    elif a <= 15 and a > 10 :
        a = 5
    elif a <= 21 and a > 15:
        a = 6
    else : a = 0

    if b == 1:
        b = 1
    elif b <= 3 and b > 1:
        b = 2
    elif b <= 7 and b > 3:
        b = 3
    elif b <= 15 and b > 7:
        b = 4
    elif b <= 31 and b > 15 :
        b = 5
    else : b = 0
    
    # print(a,b)
    if a in ftv1:
        a = ftv1[a]
    else : a = 0

    if b in ftv2:
        # print(b)
        b = ftv2[b]
    else : b = 0
    result = (a+b)*10000
    print(result)
