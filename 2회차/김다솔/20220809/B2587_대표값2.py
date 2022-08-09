import sys
sys.stdin = open('B2587.txt')

nums = sorted([int(input()) for i in range(5)])
print(sum(nums)//5, nums[2], sep='\n')