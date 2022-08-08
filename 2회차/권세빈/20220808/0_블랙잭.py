# 카드합이 21을 넘지 않는 한 최대값 만들기
# n장의 카드 m의 숫자에 가깝게, 3장의 카드합
n, m = map(int,input().split())
num = list(map(int,input().split()))
result = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum_ = num[i] + num[j] + num[k]
            if sum_ <= m:
                result.append(sum_)               
            else:
                continue
                
print(max(result))
