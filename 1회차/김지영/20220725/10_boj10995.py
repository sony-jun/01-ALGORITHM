n = int(input())
for i in range(n):
    if i % 2 == 0:
        print((n*'*'.ljust(2)))
    else : print((n*'*'.rjust(2)))