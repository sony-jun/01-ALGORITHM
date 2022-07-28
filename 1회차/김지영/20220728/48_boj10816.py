N= int(input())    # 상근이 가지고있는 숫자카드 개수
n = list(map(int,input().split()))  # 숫자카드에 적혀있는 수
M = int(input())  # 정수 M이 몇개?
m = list(map(int,input().split()))  # 정수 M 리스트
# 정수 M을 가진 숫자카드는 몇장?
# m으로 n을 세!
result = {} # 결과 리스트
for i in range(M):
    result[m[i]]=n.count(m[i])
res = ' '.join(str(i) for i in result.values())
print(res)