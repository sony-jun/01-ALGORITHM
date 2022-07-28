# 1을 1번 2를 2번 3을 3번 4를 4번 구간합 
# 1 2 3 4 5  A번째부터 B번째 숫자의 합 -> index

# 1 22 333 4444 55555 666666

A, B = map(int, input().split())

suyeol = []
for i in range(1, 46):
    for _ in range(i):
      suyeol.append(i)

print(suyeol[A-1:B])  

