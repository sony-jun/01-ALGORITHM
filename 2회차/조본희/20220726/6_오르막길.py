N = int(input())
Pi_ = list(map(int, input().split()))

uphill = 0
temp = 0
for i in range(1, len(Pi_)):
    if Pi_[i-1] < Pi_[i]:
        temp += Pi_[i] - Pi_[i-1]
    else:
        #기존 저장된 값보다 새로운 temp값이 더 클때만 교체
        if temp > uphill:
            uphill = temp
        temp = 0

# 마지막까지 오르막일경우
if temp > uphill:
    uphill = temp

print(uphill)

    