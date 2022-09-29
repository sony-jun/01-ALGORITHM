# 공약수와 최소공배수
#두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.


a ,b = map(int,input().split())

a_list=[]
b_list=[]
mr =[]
for aa in range(1,a+1): # 숫자로 비교하기떄문에 1부터 n+1로 범위를 지정해준다.
    if a%aa ==0:
        a_list.append(aa) 

for bb in range(1,b+1): # b의 약수를 구해서 a의 약수리스트에 존재한다면 mr 리스트에 추가
    if b%bb ==0:
        if bb in a_list:
            mr.append(bb)
am = max(mr)            # mr리스트중에 제일 큰 값을 am으로 지정 
dm = int(am*(a/am)*(b/am))#최소공배수는  두 값의 최대공약수 곱하기  A/최대공약수  B/최대공약수
print(am,dm) 
    
