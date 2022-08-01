n = int(input())
m = list(map(int, input().split()))
list_ = []
milk = 0

for i in m:
    if i == milk:
        list_.append(i)
        milk += 1
        if milk == 3:
            milk = 0

print(len(list_))