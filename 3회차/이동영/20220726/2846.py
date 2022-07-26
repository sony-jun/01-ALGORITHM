T = int(input())

list = list(map(int,input().split()))
distance_list = []
temp_list = []
max_distance_list = []

for i in range(0,len(list)-1):
    if list[i] < list[i+1]:
        temp_list.append(list[i])
        temp_list.append(list[i+1])
        distance_list.append(temp_list)
            
    elif list[i] >= list[i+1] and len(temp_list) != 0:
        distance_list.append(temp_list)
        temp_list = []
       
if len(distance_list) == 0:
        print(0) 
          
else:
    for j in distance_list:  
        max_distance_list.append(max(j)-min(j))
    print(max(max_distance_list))        