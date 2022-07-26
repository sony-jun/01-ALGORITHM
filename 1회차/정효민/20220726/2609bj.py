a , b = map(int , input().split())

divisor = []
divisor2 = []
divisor3 = []


# a 와 b 의 약수로 a b 를 나누고 약수를 서로 곱하면 최대 공약수

# a 와 b 의 약수로 a b 를 나눈 몫과 최대공약수를 곱하면 최소 공배수

for i in range(1 , a+1):
    if a % i == 0:
        divisor.append(i)
for y in range(1 , b + 1):
    if b % y == 0:
        divisor2.append(y)
for i in divisor:
    
    for y in divisor2 :
        
        if y == i :
            divisor3.append(y)


max_ = max(divisor3)

bottom = (a / max_)  * ( b / max_)
result2 = int(bottom) * max_ 
print(max_ , result2 , sep ='\n')
