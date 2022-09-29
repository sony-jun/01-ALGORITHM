import sys
sys.stdin = open("73_5와 6의 차이_2864.txt", "r")

a, b = input().split()

min = int(a.replace("6", "5")) + int(b.replace("6", "5"))
max = int(a.replace("5", "6")) + int(b.replace("5", "6"))

print(min, max)
