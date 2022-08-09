import sys
sys.stdin = open("대표값2.txt")

number = [int(input()) for _ in range(5)]
aver = sum(number)/ len(number)
number.sort()

print(int(aver))
print(number[2])