words = str(input())
str_list = []

for word in words:
    if word not in str_list:
        str_list.append(word)
        
str_list = ''.join(str_list)
# print(str_list) # Misp
# print(words.count(str_list[0])) # 1

cnt_list = []
for i in range(len(str_list)):
    cnt_ = words.count(str_list[i])
    cnt_list.append(cnt_)
    # print(cnt_) # 1 4 4 1

max_area = cnt_list.index(max(cnt_list))

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(str_list[max_area].upper)