# 상금 헌터
first_festival = [[5000000, 1], [3000000, 2], [2000000, 3], [500000, 4], [300000, 5], [100000, 6]]
second_festival = [[5120000, 1], [2560000, 2], [1280000, 4], [640000, 8], [320000, 16]]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    rate = 0
    if a <= 21 and a > 0:
        for i in first_festival:
            rate += i[1]
            if a <= rate:
                a = i[0]
                rate = 0
                break
    else:
        a = 0
    if b <= 31 and b > 0:
        for j in second_festival:
            rate += j[1]
            if b <= rate:
                b = j[0]
                rate = 0
                break
    else:
        b = 0
    print(a + b)