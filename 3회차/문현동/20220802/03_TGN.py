import sys
sys.stdin = open("03_TGN.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    nums = [*map(int, sys.stdin.readline().split())]
    if nums[0] + nums[2] < nums[1]:
        print("advertise")
    elif nums[0] + nums[2] == nums[1]:
        print("does not matter")
    else:
        print("do not advertise")