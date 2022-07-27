# https://www.acmicpc.net/problem/1157

word = input().upper()
my_dict = {}

for char in word:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

max_alpabet = max(my_dict, key = my_dict.get)
cnt = 0
for i in my_dict:
    if my_dict[i] == my_dict[max_alpabet]:
        cnt +=1 
        
if cnt == 1:
    print(max_alpabet)
else:
    print('?')