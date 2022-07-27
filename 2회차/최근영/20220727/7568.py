N = int(input())
all_list=[]
cnt_list=[]
for i in range(1,N+1):
    all_list.append(list(map(int,input().split())))
    cnt_list.append(1)
print(cnt_list)
for i in range(0,len(all_list)-1):
    for j in range(1,len(all_list)):
        if all_list[i][0] > all_list[j][0] and all_list[i][1] > all_list[j][1]:
            cnt_list[i] += 1
        else:
            continue

print(cnt_list)
