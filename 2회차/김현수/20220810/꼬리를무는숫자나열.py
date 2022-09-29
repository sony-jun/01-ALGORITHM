import sys
sys.stdin = open("꼬리를무는숫자나열.txt")

a, b = map(int,input().split())
a = a - 1
b = b - 1
# while True:
#     list_1 = []
#     list_2 = []
#     list_3 = []
#     list_4 = []

x = abs(b // 4 - a // 4) #8 - 2
y = abs(b % 4 - a % 4) #0 - 2

print(x + y)