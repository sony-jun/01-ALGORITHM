a, b = map(int, input().split())

if a > b:
    big = a
    small = b
else:
    big = b
    small = a

yaksoo = 1

for i in range(2, small + 1):
    if (b % i == 0) and (a % i == 0):
        yaksoo = i
beasoo = big * small // yaksoo
print(yaksoo)
print(beasoo)
