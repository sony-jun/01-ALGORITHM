#반복문에서 받은 값을 x,y따로  비교해야하는데 그러려면 
# 다음 for에서 해야하나.
#무게와 키 리스트를 따로 만들어서 각각에 등수를...?아니고
#
n = int(input())
li = []
for _ in range(n):
    x, y = map(int,input().split())
    li.append((x,y))

for i in li:
    rank = 1
    for j in li:
        if i[0] != j[0] and i[1] != j[1]:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank,end = ' ')
    


