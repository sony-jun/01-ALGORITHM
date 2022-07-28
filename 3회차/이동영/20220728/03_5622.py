# 사전 만들기
dict = {}
k = 3

# A ~ O 까지 
for i in range(65,80):
    dict[chr(i)] = k
    
    if i % 3 == 1:
        k += 1
k = 8
# P ~ S 까지    
for i in range(80,84):
    dict[chr(i)] = k

# T ~ V 까지
k = 9
for i in range(84,87):
    dict[chr(i)] = k

# W ~ Z 까지     
k = 10
for i in range(87,91):
    dict[chr(i)] = k
    
#=================================================================

N = list(input())

numbers_list = []

for alphabet in N:
    numbers_list.append(dict[alphabet])

print(sum(numbers_list))