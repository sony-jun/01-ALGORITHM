#N에서 생성자를 구하려면 1~N까지의 숫자들을 i로 잡고 
# if ~에서 자릿수를 더한 값이 N이 나오게 조건을 건뒤 
# 반복문을 돌리는데 가장 먼저 나오는 i가 답이고 그 이후는 break로 멈춰줌
# 구글-갓의 힘을 빌림... 대신 이해하려고 노력함
N=int(input())
for i in range(1,N+1):
    list_=list(map(int,str(i)))
    ans=i+sum(list_)
    if ans==N:
        print(i)
        break
    if i== N:
        print(0)    
