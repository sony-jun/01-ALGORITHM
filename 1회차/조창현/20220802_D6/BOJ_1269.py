import sys

sys.stdin = open("1269input.txt")

at, bt = map(int, input().split())
# a = set(input().split(' '))
# b = set(input().split(' '))

# print(len(a ^ b))

################################################

print(len(set(input().split(' ')) ^ set(input().split(' '))))