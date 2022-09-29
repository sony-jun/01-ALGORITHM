t = int(input())

for i in range(t):
    a, b =map(int,input().split())
    a_money = 0
    b_money = 0
    if a == 1:
        a_money+=500*10000
    elif a == 0:
        a_money = 0
    elif a <= 3:
        a_money+=300*10000
    elif a <= 6:
        a_money+=200*10000
    elif a <= 10:
        a_money+=50*10000
    elif a <= 15:
        a_money+=30*10000
    elif a <= 21:
        a_money+= 10*10000

    if b ==1:
        b_money+=512*10000
    elif b == 0:
        b_money = 0
    elif b<=3:
        b_money+=256*10000
    elif b<=7:
        b_money+=128*10000
    elif b<=15:
        b_money+=64*10000
    elif b<=31:
        b_money+=32*10000

    result = a_money+b_money
    print(result)
    

    # t = int(input())
    # for i in range(t):
    #     a,b = map(int,input().split())

    #     for i in range(1,7):
            