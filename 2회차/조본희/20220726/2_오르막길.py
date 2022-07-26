N = int(input())
Pi_ = list(map(int, input().split()))

uphill = 0
temp = 0
for i in range(1, len(Pi_)):
    if Pi_[i-1] < Pi_[i]:
        temp += Pi_[i] - Pi_[i-1]
    else:
        if temp > uphill:
            uphill = temp
        temp = 0
if temp > uphill:
    uphill = temp
print(uphill)

    