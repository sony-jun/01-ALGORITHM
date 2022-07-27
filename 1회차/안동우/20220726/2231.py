
a,b= map(int, input().split())

#배수 약수 구하고
#공약수 공배 구하고
#최대공약수 최소공배수구하고
#출력
a=a
b=b
measure=[] #공약수
Drainage1=[]#공배수
Drainage2=[]

for i in  range(1,b+1):
    if a%i== 0 and b%i==0:
        measure.append(i)
        measure.sort(i)
print(measure) 
for j in range(1,a+1):
    if j*a:
        Drainage1.append(j*a)
    if j*b:
        Drainage2.append(j*b)
Drainage3=list(set(Drainage1).intersection(Drainage2))
Drainage3.sort()
print(Drainage3[0])
