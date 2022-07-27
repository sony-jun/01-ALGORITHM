# https://www.acmicpc.net/problem/1157

str_ = input()
up_str = []
list_i = 0
count_ = {}

for s in str_:
    up_str.append(s.upper())
    #up_str[list_i] = ord(up_str[list_i])
    if up_str[list_i] in count_:
        count_[up_str[list_i]] +=1
    else:
        count_[up_str[list_i]] = 1
    list_i+=1
max_ = {k for k,v in count_.items() if max(count_.values())==v}   #{'k'}
if len(max_) > 1 :
    print('?')
else:
    print(max(count_)) # 최대값이 여러개일 때 앞에 것만 출력됨


#print(count_.items()) # dict_items([('M', 1), ('I', 4), ('S', 4), ('P', 1)])
#print(count_.values()) # dict_values([1, 4, 4, 1])


   
    


    

#set_ = set(up_str)
#print(set_)