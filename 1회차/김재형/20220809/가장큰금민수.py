

N = int(input())


while True:
    a = True
    for i in str(N):
        if i != '4' and i != '7':
            a = False
            N -= 1
    if a:
        print(N)
        break

