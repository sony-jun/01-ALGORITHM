a = int(input())
list_ = list(map(int, input().split()))
road = list_[::-1]

o_list = []
hill = 0
for i in range(a - 1):
    # hill = 0
    if road[i] > road[i + 1]:
        hill += road[i] - road[i + 1]
        
    elif road[i] <= road[i + 1]:
        o_list.append(hill)
        hill = 0
        
o_list.append(hill)

print(max(o_list))