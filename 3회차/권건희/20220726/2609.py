# 두개 자연수 입력 받고 n1,n2=map(int,(input().split()))
# 최대 공약수는 어떻게 구할까?
# 같은 i로 나눴을때 0이 되는 것을 찾아야함--->range(min(n1,n2),1,-1)
# 최소 공배수는 반대로 I를 나눴을때 0이 되는 최소의 수를 찾아야함---> range(max(a,b),a*b+1)

n1,n2=map(int,(input().split()))
for i in range(min(n1,n2),0,-1):
    if n1%i==0 and n2%i==0:
        print(i)  
        break
# 최소 공배수는 최대 공약수 *a=n1, n2=최대 공약수 *b 에서, 최대공약수*a*b로도 구할 수 있다. (런타임 에러 생기면 이거 먼저 생각해보기...)    
print(int((n1/i)*(n2/i)*(i)))

 
