n = int(input())

for _ in range(n):
    list_ = []
    list_ = (list(map(int,input().split())))
    
    list_ = sorted(list_, reverse=True)

    print(list_[2])