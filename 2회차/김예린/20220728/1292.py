# 쉽게 푸는 문제

# 해결
a, b = map(int, input().split())

nums = []

for i in range(1, b +1):
    for j in range(i):
            nums.append(i)

print(sum(nums[a-1:b]))


# 오답
# 시간초과
a, b = map(int, input().split())

nums = []

for i in range(1, b + 1 // 2):  # 범위를 줄이기 위해 2를 나눴지만, 더 큰 입력값에서 실행할 수 없음
    nums.append(i)              # 시간 초과 원인
    for j in range(i):
        if i != nums.count(i):  # 시간 초과 원인
            nums.append(i)      # appen(i)로 충분히 구현 가능. if문 필요 없음

print(sum(nums[a-1:b]))

# while문 활용
N = 0
while len(nums) < B :
    for _ in range(N):
        nums.append(N)
    N += 1
print(nums, len(nums))

