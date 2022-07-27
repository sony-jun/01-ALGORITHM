T = int(input())
total = []
i = 0
for a in range(T) :
    number = list(map(int , input().split()))
    total.append(number)
    
    for a in total :
        if 5> a[0]:
            i += 1
            print(i)

