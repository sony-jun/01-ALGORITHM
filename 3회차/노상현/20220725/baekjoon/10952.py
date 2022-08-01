while(True):
    a, b = map(int, input().split())
    0 < a and 10>b

    if  a == 0 and b == 0:
        break
    else:
        print(a+b)