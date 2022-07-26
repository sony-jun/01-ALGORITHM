n = int(input())
high = list(map(int, input().split()))
high = high[::-1]
high_g = []
high_p =0
low_p = 0
for i in range(n - 1):
    if high[i] > high[i + 1]:
        if high[i] > high_p :
            high_p = high[i]
        low_p = high[i + 1]
        high_g.append(high_p - low_p)
    else:
        high_g.append(high_p - low_p)
        high_p = 0
print(max(high_g))