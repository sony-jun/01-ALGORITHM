# 문제 : 최대 오르막길 구하기
# 입력 : 5
#       1 2 1 4 6
# 출력 : 5

n = int(input())
num = list(map(int, input().split()))

way = num[0]
high = 0
save = 0


for i in num:
    if way < i:
        high += i - way
    if way >= i:
        save = max(save, high)
        high = 0
    way = i

print(max(high, save))
