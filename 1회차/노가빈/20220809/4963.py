while True:
    n1,n2 = map(int,input().split(' '))

    if n1==0 and n2 == 0:
        break


    lst = []
    for i in range(n2):
        lst.append(list(map(int,input().split(' '))))
    print(lst)
    