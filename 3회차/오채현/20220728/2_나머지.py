nums = []
remains = []

for i in range(10):
    n = int(input())
    nums.append(n % 42)
    result = set(nums)
print(len(result))

    # for num in nums:
    #     if num % 42 not in remains:
    #         remains.append(num % 42)
# print(len(remains))