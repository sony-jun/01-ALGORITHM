
list_ = []

for i in range(10) :
    num = int(input())
    list_.append(num % 42) 
a = set(list_) #내어쓰기를 해야지, 한꺼번에 출력 됨 
print(len(a))



# a = 20
# b = 42
# c = a%b
# print(c)