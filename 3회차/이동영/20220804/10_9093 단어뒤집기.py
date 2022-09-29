n = int(input())

for _ in range(n):
    list_ = []
    list_ = list(input().split())

    for i in list_:
        print(i[::-1], end=' ')
    print() 
        