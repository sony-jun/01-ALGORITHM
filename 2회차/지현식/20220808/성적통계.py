import sys

input = sys.stdin.readline

for test_case in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    k = nums.pop(0)
    nums.sort(reverse=True)
    gap = 0
    for i in range(k - 1):
        gap = max(gap, nums[i] - nums[i + 1])
    print(f"{'Class'} {test_case}")
    print(f"{'Max'} {max(nums)}, {'Min'} {min(nums)}, {'Largest gap'} {gap}")