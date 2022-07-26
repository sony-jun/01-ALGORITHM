a, b= map(int,input().split())
tmp = []
for i in range(min(a, b), 0, -1): # 두개의 수 중에서 작은 수가 큰수의 약수가 되어 작은 수 그 자체로 최대 공약수 일수도 있기 때문에  min()사용. ex) 2, 4
    if a % i == 0 and b % i == 0: # 공약수 중에서 제일 큰 수를 찾는 문제로 가장 첫번째 약수가 최대 공약수가 됨.-> 내림차순으로 for문 진행.
        tmp.append(i)
print(tmp[0])
print(tmp[0]*(a//tmp[0])*(b//tmp[0]))