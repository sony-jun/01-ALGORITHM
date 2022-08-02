import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

set1_ = set(map(int, input().split()))
set2_ = set(map(int, input().split()))

print(len(set1_- set2_) + len(set2_ - set1_))