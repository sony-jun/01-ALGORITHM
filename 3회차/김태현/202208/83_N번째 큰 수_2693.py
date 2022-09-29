import sys
sys.stdin = open("83_N번째 큰 수_2693.txt", "r")

T = int(input())

for tc in range(T):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[2])