T = input()
T=T.upper()
check_list =[]
for i in T:
    check_list.append(str(ord(i)))
    
str_dict={}
for j in check_list:
    str_dict[j] = str_dict.get(j,0) + 1
val_list=[]
key_list=[]
for k,v in str_dict.items():
    key_list.append(k)
    val_list.append(v)

max_val = max(val_list)
position = val_list.index(max_val)
cnt = 0

for l in val_list:
    if l == max_val:
        cnt += 1

if cnt >= 2:
    print("?")
else:
    print(chr(int(key_list[position])))