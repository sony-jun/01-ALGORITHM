import sys
input = sys.stdin.readline

for i in range(int(input())):
    numbers_ = list(map(int, input().split()))
    numbers_ = sorted(numbers_, reverse= True)
    print(numbers_[2])