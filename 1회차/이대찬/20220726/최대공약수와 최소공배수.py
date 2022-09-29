a,b = map(int,(input().split(' ')))

a_= [] #a 약수
b_= [] #b 약수

ab= 0 #최대공약수

for i in range(1,a+1):
    if a % i == 0:
        a_.append(i)

for i in range(1,b+1):
    if b % i == 0:
        b_.append(i)
        
for i in a_:
    if i in b_ and i > ab:
        ab = i




 





