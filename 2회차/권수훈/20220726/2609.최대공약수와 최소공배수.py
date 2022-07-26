number_a,number_b = map(int,(input().split()))
# 두수를 int로 입력받는다
# 약수는 나누었을때 나머지가 0이되는 수 이니까
# 첫번째 입력받는수를 i 로 한번씩 나누고 나머지가 0이면 리스트안에 넣어주었다    
a_result=[]

for i in range(1,number_a+1):
    if number_a % i == 0:
        a_result.append(i)


b_result=[]
# 약수는 나누었을때 나머지가 0이되는 수 이니까
# 두번째 입력받는수를 j 로 한번씩 나누고 나머지가 0이면 리스트안에 넣어주었다  
for j in range(1,number_b+1):
    if number_b % j == 0:
        b_result.append(j)
 


# 두개의 리스트를 교집합하여 & 
max_reult =  list(set(a_result) & set(b_result))
print(max_reult.pop())
# 약수a 약수b의 교집합 리스트의 마지막자리 (가장큰수)를 출력했다
# 최소 공배수 a*b % 최대공약수
# a b 의 
