T = int(input())

for test in range(1, T+1):
    M = list(map(int, input().split()))
    for i in M:
        mul_ = 0
        sum_ = 0
        result = 0
        if i % 2 == True:
            mul_ += (i * 2)
            #print(mul_)
        elif i % 2 == 0:
            i += sum_
            print(sum_)
        result = (mul_ + sum_)
