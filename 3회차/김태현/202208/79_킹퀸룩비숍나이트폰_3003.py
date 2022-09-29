import sys
sys.stdin = open("79_킹퀸룩비숍나이트폰_3003.txt", "r")

chess = [1, 1, 2, 2, 2, 8]

nums = list(map(int, input().split()))

for i in range(len(nums)):
    if nums[i] > chess[i]:
        print(chess[i] - nums[i], end = " ")
    elif nums[i] < chess[i]:
        print(chess[i] - nums[i], end = " ")
    else:
        print(0, end = " ")