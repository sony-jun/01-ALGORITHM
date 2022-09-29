# 수열을 넣을 빈 리스트 생성
suyeol = []

# 1부터 1001까지 순호
for i in range(1, 1001):
    # 수열 리스트에 i를 i만큼 추가
    suyeol.extend([i] * i)

a, b = map(int, input().split())
sum = 0

# 수열 리스트의 인덱스는 0부터 시작하기 때문에 a-1부터 b까지 순회
for i in range(a-1, b):
    # 순회한 수열 값을 sum에 더함
    sum += suyeol[i]

print(sum)