

# a = input().upper()
# result = {}
# z =[]
# #for char in a:
# #    pass
# for lenchar in range(len(a)):
        
    
#     result[a[lenchar]] = result.get(a[lenchar] , 0) + 1
# print(result.count(max))



    

# print(max(result , key = result.get))

a = input().upper()
cnt = []
setforword = list(set(a))

for word_list in setforword:
    count_list = a.count(word_list)
    cnt.append(count_list)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(setforword[cnt.index(max(cnt))])
