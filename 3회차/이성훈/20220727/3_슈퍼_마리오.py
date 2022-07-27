# https://www.acmicpc.net/problem/2851
import sys

sys.stdin = open("3_슈퍼_마리오.txt")

sum_ = 0

for i in range(10) :
    num = int(input())
    sum_ += num

    if sum_ == 100:
        break
    else:
        if (sum_ -100) > (100 - (sum_- num)):   # 왼쪽 : 100 초과인 가까운값  오른쪽 : 100 미만인 가까운 값
            sum_ -= num                         # sum_ -100이 100 - (sum_ - num)보다 크다는 의미는 더 멀다는 의미이므로 이전 값을 채택
            break

print(sum_)

    
