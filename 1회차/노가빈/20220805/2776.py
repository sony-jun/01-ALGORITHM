t = int(input())

for i in range(t):
    num = int(input())
    numlist1=list(map(int,input().split(' ')))
    num = int(input())
    numlist2=list(map(int,input().split(' ')))

    for z in numlist2:
        if z in numlist1:
            print(1)
        else:
            print(0)

