t = int(input())  
# input the number of cases you want to run at 't'
s_list = []

for s in range(t):  
    a,b = map(int,input().split())
    s_list.append((a, b))

for i in s_list:
    place = 1
    for k in s_list:
        if i[0] < k[0] and i[1] < k[1]:
            place += 1
    
    print(place, end = ' ')
