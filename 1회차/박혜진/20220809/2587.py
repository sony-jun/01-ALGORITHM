# 5개의 자연수 입력받기
from statistics import quantiles

nums = []

for _ in range(5) :
    nums.append(int(input()))

print(sum(nums)//5)
print(int(quantiles(nums)[1]))