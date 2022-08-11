import sys

sys.stdin = open("_2495.txt", "r")


for _ in range(3):
    nums = input()
    X = nums[0]
    answer = []
    cnt = 0
    for num in nums:
        if num == X:
           cnt += 1
        else:
            X = num
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    print(max(answer))