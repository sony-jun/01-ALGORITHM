
# nums = [5, 2, 3, 4, 1]


# for n in nums:
#     nums.append(int(input()))
# nums.sort()
# for i in nums:
#     print(i)


T = int(input())
nums = []

for i in range(T):
    nums.append(int(input()))
    print(nums)
nums.sort()
for n in nums:
    print(n)