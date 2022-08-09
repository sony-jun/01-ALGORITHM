# 손님의 수 n
n = int(input())

# 손님이 원하는 번호
nums = list(map(int, input().split()))
set_nums = len(set(nums))

no = n - set_nums

print(no)