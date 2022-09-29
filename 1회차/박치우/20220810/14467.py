n = int(input())
dic = dict()
count = 0
for i in range(n):
    cow ,road = map(int,input().split())
    if cow not in dic:
        dic[cow] = road
    else:
        if dic[cow] != road:
            dic[cow] = road
            count += 1
        elif dic[cow] == road:
             continue
print(count)

