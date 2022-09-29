import sys
sys.stdin = open('04_input.txt')

for _ in range(3):
    nums = input()
    cnt = 1
    maxcnt = 1

    for i in range(1, 8):
        if nums[i] == nums[i-1]:
            cnt += 1
            if cnt > maxcnt:
                maxcnt = cnt
        else:
            cnt = 1
    print(maxcnt)
