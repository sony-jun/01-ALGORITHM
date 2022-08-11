import sys
sys.stdin = open('트럭주차_input.txt')


one, two, three = map(int, input().split())

parking = [0] *101 
price = 0

for i in range(3):
    srt, fin = map(int, input().split())
    for j in range(srt-1, fin-1):
        parking[j] += 1

for k in parking:
    if k == 1:
        price += (k*one)
    if k == 2:
        price += (k*two)
    if k == 3:
        price += (k*three)
print(price)
